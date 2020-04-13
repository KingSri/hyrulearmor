from django.shortcuts import render, redirect

# these imports are strictly for use with Class-based views
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Armor, Material
from .forms import ArmorForm, WearForm


# Define the home view
def home(request):
  return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def armor_index(request):
    armor = Armor.objects.filter(user=request.user)
    return render(request, 'armor/index.html', { 'armor': armor })

@login_required
def armor_detail(request, armor_id):
    armor = Armor.objects.get(id=armor_id)
    material_armor_doesnt_have = Material.objects.exclude(id__in = armor.material.all().values_list('id'))
    wear_form = WearForm()
    context = {
        'armor': armor,
        'wear_form': wear_form,
        'material': material_armor_doesnt_have,
    }
    return render(request, 'armor/detail.html', context)

@login_required
def add_time(request, armor_id):
  # create an instance of the model using the ModelForm and POST data
  form = WearForm(request.POST)
  # validate the form
  if form.is_valid():
    # first assign the Feeding to a armor using armor_id
    new_time = form.save(commit=False)
    new_time.armor_id = armor_id
    new_time.save()
  # redirect takes the name of the URL as the first arg,
  # and any required info as a kwarg after that
  return redirect('detail', armor_id=armor_id)

# adding crud to armor models
@login_required
def new_armor(request):
  # if a post request is made to this view function
  if request.method == 'POST':
    # save the form data to a variable
    form = ArmorForm(request.POST)
    if form.is_valid():
        armor = form.save(commit=False)
        armor.user = request.user
        armor.save()
    return redirect('detail', armor.id)
  else:
    # if a get request is made to this view function,
    # create new, empty instance of the ArmorForm
    form = ArmorForm()
  # create a context dictionary
  context = { 'form': form }
  # pass the form (through context) to the armor_form template
  return render(request, 'armor/armor_form.html', context)

@login_required
def armor_update(request, armor_id):
  # Select the armor that we're updating from the DB
  armor = Armor.objects.get(id=armor_id)

  # If the request is a POST
  if request.method == "POST":
    form = ArmorForm(request.POST, instance=armor)
    if form.is_valid():
      armor = form.save()
      return redirect('detail', armor.id)
  # If not a POST, create the form
  else:
    form = ArmorForm(instance=armor)
  # Render the form by sending the context to our existing template
  return render(request, 'armor/armor_form.html', { 'form': form })

@login_required
def armor_delete(request, armor_id):
  # Select the armor and delete it
  Armor.objects.get(id=armor_id).delete()
  # Redirect the user
  return redirect('index')

@login_required
def assoc_material(request, armor_id, material_id):
  # Note that you can pass a material's id instead of the whole object
  Armor.objects.get(id=armor_id).material.add(material_id)
  return redirect('detail', armor_id=armor_id)

def signup(request):
  error_message = ''
  if request.method == 'POST':
    # This is how to create a 'user' form object
    # that includes the data from the browser
    form = UserCreationForm(request.POST)
    if form.is_valid():
      # This will add the user to the database
      user = form.save()
      # This is how we log a user in via code
      login(request, user)
      return redirect('index')
    else:
      error_message = 'Invalid sign up - try again'
  # A bad POST or a GET request, so render signup.html with an empty form
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)
  # material model views

class MaterialList(LoginRequiredMixin, ListView):
    model = Material

class MaterialDetail(LoginRequiredMixin, DetailView):
    model = Material

class MaterialCreate(LoginRequiredMixin, CreateView):
    model = Material
    fields = '__all__'

class MaterialUpdate(LoginRequiredMixin, UpdateView):
    model = Material
    fields = ['name', 'color', 'description']

class MaterialDelete(LoginRequiredMixin, DeleteView):
    model = Material
    success_url = '/material/'

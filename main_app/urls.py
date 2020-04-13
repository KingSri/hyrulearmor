from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('armor/', views.armor_index, name='index'),
    path('armor/new/', views.new_armor, name='new_armor'),
    path('armor/<int:armor_id>/', views.armor_detail, name='detail'),
    path('armor/<int:armor_id>/edit/', views.armor_update, name='armor_update'),
    path('armor/<int:armor_id>/delete/', views.armor_delete, name='armor_delete'),
    path('armor/<int:armor_id>/add_time', views.add_time, name='add_time'),
    path('armor/<int:armor_id>/assoc_material/<int:material_id>/', views.assoc_material, name='assoc_material'),

    #full Crud for Upgrade materials
    path('material/', views.MaterialList.as_view(), name='material_index'),
    path('material/<int:pk>/', views.MaterialDetail.as_view(), name='material_detail'),
    path('material/create/', views.MaterialCreate.as_view(), name='material_create'),
    path('material/<int:pk>/update/', views.MaterialUpdate.as_view(), name='material_update'),
    path('material/<int:pk>/delete/', views.MaterialDelete.as_view(), name='material_delete'),
    path('accounts/signup', views.signup, name='signup'),

]

from django.db import models
from django.urls import reverse
from datetime import date

# Create your models here.
TIME = (
    ('M', 'Morning'),
    ('D','Day'),
    ('N', 'Night')
)

class Material(models.Model):
    name = models.CharField(max_length=50)
    color = models.CharField(max_length=20)
    description = models.TextField(max_length=250)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("material_detail", kwargs={'pk': self.id})


class Armor(models.Model):
    name = models.CharField(max_length=100)
    function = models.CharField(max_length=150)
    description = models.TextField(max_length=250)
    ap = models.IntegerField()
    material = models.ManyToManyField(Material)

    def __str__(self):
        return self.name

    def worn_today(self):
        return self.wear_set.filter(date=date.today()).count() >= len(TIME)

    # def fed_for_today(self):
    #     return self.wear_set.filter(date=date.today()).count() >= len(MEALS)



class Wear(models.Model):
    date = models.DateField('Date Worn')
    time = models.CharField(
    max_length=1,
        choices=TIME,
        default=TIME[0][0]
    )
    armor = models.ForeignKey(Armor, on_delete=models.CASCADE)

    def __str__(self):
        return f"Wore during {self.get_time_display()} on {self.date}"

    class Meta:
        ordering = ['-date']

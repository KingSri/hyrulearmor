# Generated by Django 3.0.5 on 2020-04-12 08:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_auto_20200412_0813'),
    ]

    operations = [
        migrations.AddField(
            model_name='armor',
            name='material',
            field=models.ManyToManyField(to='main_app.Material'),
        ),
    ]
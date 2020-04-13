# Generated by Django 3.0.5 on 2020-04-12 08:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_wear'),
    ]

    operations = [
        migrations.CreateModel(
            name='Material',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('color', models.CharField(max_length=20)),
                ('description', models.TextField(max_length=250)),
            ],
        ),
        migrations.AlterModelOptions(
            name='wear',
            options={'ordering': ['-date']},
        ),
        migrations.AlterField(
            model_name='wear',
            name='date',
            field=models.DateField(verbose_name='Date Worn'),
        ),
    ]
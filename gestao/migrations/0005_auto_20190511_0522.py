# Generated by Django 2.1.2 on 2019-05-11 05:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestao', '0004_auto_20190511_0520'),
    ]

    operations = [
        migrations.AlterField(
            model_name='animal',
            name='sexo',
            field=models.CharField(choices=[('M', 'Macho'), ('F', 'Fêmea')], max_length=1),
        ),
    ]

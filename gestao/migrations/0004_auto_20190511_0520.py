# Generated by Django 2.1.2 on 2019-05-11 05:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestao', '0003_auto_20190511_0344'),
    ]

    operations = [
        migrations.AlterField(
            model_name='animal',
            name='sexo',
            field=models.CharField(choices=[('Abate', 'Macho'), ('Abate', 'Fêmea')], max_length=1),
        ),
        migrations.AlterField(
            model_name='animal',
            name='tipagem',
            field=models.CharField(choices=[('Abate', 'Abate'), ('Matriz', 'Matriz')], max_length=6),
        ),
    ]

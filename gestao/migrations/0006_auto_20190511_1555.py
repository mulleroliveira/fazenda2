# Generated by Django 2.1.2 on 2019-05-11 15:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gestao', '0005_auto_20190511_0522'),
    ]

    operations = [
        migrations.RenameField(
            model_name='animal',
            old_name='fazenda',
            new_name='farm',
        ),
        migrations.RenameField(
            model_name='animal',
            old_name='sexo',
            new_name='sex',
        ),
        migrations.RenameField(
            model_name='animal',
            old_name='tipagem',
            new_name='typing',
        ),
    ]

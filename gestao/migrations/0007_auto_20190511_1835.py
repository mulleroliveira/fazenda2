# Generated by Django 2.1.2 on 2019-05-11 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestao', '0006_auto_20190511_1555'),
    ]

    operations = [
        migrations.AlterField(
            model_name='creator',
            name='cpf',
            field=models.CharField(blank=True, max_length=11, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='creator',
            name='date_birth',
            field=models.DateField(blank=True, null=True),
        ),
    ]
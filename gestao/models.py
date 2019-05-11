from django.db import models

class Creator(models.Model):
    name = models.CharField(max_length=20)
    cpf = models.CharField(max_length=11, unique=True)
    date_birth = models.DateField(null=True)

    def __str__(self):
        return self.name

class Farm(models.Model):
    name = models.CharField(max_length=20)
    address = models.CharField(max_length=20)
    creator = models.ForeignKey(Creator, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Animal(models.Model):

    typing_choices = (
        ("Abate", "Abate"),
        ("Matriz", "Matriz")
    )

    sex_choices = (
        ("M", "Macho"),
        ("F", "Fêmea")
    )

    name = models.CharField(max_length=20)
    sex = models.CharField(max_length=1, choices=sex_choices)
    typing = models.CharField(max_length=6, choices=typing_choices)
    farm = models.ForeignKey(Farm, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
from django.db import models

class Creator(models.Model):
    name = models.CharField(max_length=20)
    cpf = models.CharField(max_length=11, unique=True)
    date_birth = models.DateField()

    def __str__(self):
        return self.name

class Farm(models.Model):
    name = models.CharField(max_length=20)
    address = models.CharField(max_length=20)
    creator = models.ForeignKey(Creator, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Animal(models.Model):

    tipagem_choices = (
        ("A", "Abate"),
        ("M", "Matriz")
    )

    sexo_choices = (
        ("M", "Macho"),
        ("F", "Fêmea")
    )

    name = models.CharField(max_length=20)
    sexo = models.CharField(max_length=1, choices=sexo_choices)
    tipagem = models.CharField(max_length=1, choices=tipagem_choices)
    fazenda = models.ForeignKey(Farm, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
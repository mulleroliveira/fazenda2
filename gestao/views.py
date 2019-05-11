from django.shortcuts import render, redirect
from . models import Animal
from . forms import FormAnimal

def home(request):
    return render(request, 'home/home.html')

def animals(request):
    animals = Animal.objects.all()
    return render(request, 'animals/list.html', {'animals':animals})


def delete_animal(request, id_animal):
    animal = Animal.objects.get(pk=id_animal)
    animal.delete()
    return redirect('/gestao/animais/')

def register_animal(request):
    if request.method == 'POST':
        form = FormAnimal(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/gestao/animais/')
        else:
            return render(request, 'animals/register.html', {'form':form})
    else:
        form = FormAnimal()
        return render(request, 'animals/register.html', {'form':form})

def edit_animal(request, id_animal):
    if request.method == 'POST':
        animal = Animal.objects.get(pk=id_animal)
        form = FormAnimal(request.POST, instance=animal)
        if form.is_valid():
            form.save()
            return redirect('/gestao/animais/')
        else:
            return render(request, 'animals/edit.html', {'form':form, 'animal':animal})
    else:
        animal = Animal.objects.get(pk=id_animal)
        form = FormAnimal(instance=animal)
        return render(request, 'animals/edit.html', {'form':form,'animal':animal})
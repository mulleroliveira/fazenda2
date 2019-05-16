from django.shortcuts import render, redirect
from . models import Animal, Creator, Farm
from . forms import FormAnimal, FormCreator, FormFarm
from django.http import HttpResponse


def home(request):
    return render(request, 'home/home.html')

def animals(request):
    if request.method == 'POST':
        form = request.POST.get('select')
        animals = Animal.objects.all().order_by(form)
        return render(request, 'animals/list.html', {'animals':animals})
    else:
        animals = Animal.objects.all()
        return render(request, 'animals/list.html', {'animals':animals})


def delete_animal(request, id_animal):
    animal = Animal.objects.get(pk=id_animal)
    animal.delete()
    return redirect('/gestao/animals/')

def register_animal(request):
    if request.method == 'POST':
        form = FormAnimal(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/gestao/animals/')
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
            return redirect('/gestao/animals/')
        else:
            return render(request, 'animals/edit.html', {'form':form, 'animal':animal})
    else:
        animal = Animal.objects.get(pk=id_animal)
        form = FormAnimal(instance=animal)
        return render(request, 'animals/edit.html', {'form':form,'animal':animal})

def creators(request):
    if request.method == 'POST':
        form = request.POST.get('name')
        creators = Creator.objects.filter(name__icontains=form)
        return render(request, 'creators/list.html', {'creators':creators})
    else:
        creators = Creator.objects.all()
        return render(request, 'creators/list.html', {"creators":creators})

def delete_creator(request, id_creator):
    creator = Creator.objects.get(pk=id_creator)
    creator.delete()
    return redirect('/gestao/creators/')

def register_creator(request):
    if request.method == 'POST':
        form = FormCreator(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/gestao/creators/')
        else:
            return render(request, 'creators/register.html', {'form':form})
    else:
        form = FormCreator()
        return render(request, 'creators/register.html', {'form':form})

def edit_creator(request, id_creator):
    if request.method == 'POST':
        creator = Creator.objects.get(pk=id_creator)
        form = FormCreator(request.POST, instance=creator)
        if form.is_valid():
            form.save()
            return redirect('/gestao/creators/')
        else:
            return render(request, 'creators/edit.html', {'form':form, 'creator':creator})
    else:
        creator = Creator.objects.get(pk=id_creator)
        form = FormCreator(instance=creator)
        return render(request, 'creators/edit.html', {'form':form,'creator':creator})

def farms(request):
    farms = Farm.objects.all()
    return render(request, 'farms/list.html', {'farms':farms})

def delete_farm(request, id_farm):
    farm = Farm.objects.get(pk=id_farm)
    farm.delete()
    return redirect('/gestao/farms/')

def register_farm(request):
    if request.method == 'POST':
        form = FormFarm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/gestao/farms/')
        else:
            return render(request, 'farms/register.html', {'form':form})
    else:
        form = FormFarm()
        return render(request, 'farms/register.html', {'form':form})

def edit_farm(request, id_farm):
    if request.method == 'POST':
        farm = Farm.objects.get(pk=id_farm)
        form = FormFarm(request.POST, instance=farm)
        if form.is_valid():
            form.save()
            return redirect('/gestao/farms/')
        else:
            return render(request, 'farms/edit.html', {'form':form, 'farm':farm})
    else:
        farm = Farm.objects.get(pk=id_farm)
        form = FormFarm(instance=farm)
        return render(request, 'farms/edit.html', {'form':form, 'farm':farm})
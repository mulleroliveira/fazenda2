from django.shortcuts import render, redirect
from . models import Animal, Creator, Farm
from . forms import FormAnimal, FormCreator, FormFarm

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

def creators(request):
    creators = Creator.objects.all()
    return render(request, 'creators/list.html', {"creators":creators})

def delete_creator(request, id_creator):
    creator = Creator.objects.get(pk=id_creator)
    creator.delete()
    return redirect('/gestao/criadores/')

def register_creator(request):
    if request.method == 'POST':
        form = FormCreator(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/gestao/criadores/')
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
            return redirect('/gestao/criadores/')
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
    return redirect('/gestao/fazendas/')

def register_farm(request):
    if request.method == 'POST':
        form = FormFarm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/gestao/fazendas/')
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
            return redirect('/gestao/fazendas/')
        else:
            return render(request, 'farms/edit.html', {'form':form, 'farm':farm})
    else:
        farm = Farm.objects.get(pk=id_farm)
        form = FormFarm(instance=farm)
        return render(request, 'farms/edit.html', {'form':form, 'farm':farm})
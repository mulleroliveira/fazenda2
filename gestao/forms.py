from django.forms import ModelForm, TextInput, Select, DateInput
from . models import Animal, Farm, Creator

class FormAnimal(ModelForm):
    class Meta:
        model = Animal
        fields = ('__all__')
        widgets = {
            'name': TextInput(attrs={'class':'form-control'}),
            'sex': Select(attrs={'class':'form-control'}),
            'typing': Select(attrs={'class':'form-control'}),
            'farm': Select(attrs={'class':'form-control'})}

class FormCreator(ModelForm):
    class Meta:
        model = Creator
        fields = ('__all__')
        widgets = {
            'name': TextInput(attrs={'class':'form-control'}),
            'cpf': TextInput(attrs={'class':'form-control'}),
            'date_birth': DateInput(attrs={'class':'form-control'})}

class FormSearch(ModelForm):
    class Meta:
        model = Creator
        fields = ('name',)

class FormFarm(ModelForm):
    class Meta:
        model = Farm
        fields = ('__all__')
        widgets = {
            'name': TextInput(attrs={'class':'form-control'}),
            'address': TextInput(attrs={'class':'form-control'}),
            'creator': Select(attrs={'class':'form-control'})}

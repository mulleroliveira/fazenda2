from django.forms import ModelForm, TextInput, Select
from . models import Animal, Farm, Creator

class FormAnimal(ModelForm):
    class Meta:
        model = Animal
        fields = ('__all__')
        widgets = {
            'name': TextInput(attrs={'class':'form-control'}),
            'sexo': Select(attrs={'class':'form-control'}),
            'tipagem': Select(attrs={'class':'form-control'}),
            'fazenda': Select(attrs={'class':'form-control'})}
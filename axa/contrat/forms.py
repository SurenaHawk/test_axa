from django.forms import ModelForm
from .models import Projet
from django import forms

# class RisqueForm(forms.Form):
#     opportunity_member = forms.CharField(label = 'Numéro opportunité', max_length=10)
#     client_name = forms.CharField(label = 'Nom Client')
#     siret_number = forms.IntegerField()
#     siren_number = forms.IntegerField()
#     affaire = forms.CharField()
#     reference = forms.CharField()
#     intermediaire = forms.CharField()
#     short_description = forms.CharField()
#     image = forms.ImageField()
#     coassurance = forms.BooleanField()
#     operation_adresse = forms.CharField()
#     operation_description = forms.Textarea()
#     price_operation = forms.DecimalField()

class RisqueForm(ModelForm):
    class Meta:
        model = Projet
        fields = '__all__'

    # opportunity_member = forms.CharField(label = 'Numéro opportunité', max_length=10)
    # client_name = forms.CharField(label = 'Nom Client')
    # siret_number = forms.IntegerField()
    # siren_number = forms.IntegerField()
    # affaire = forms.CharField()
    # reference = forms.CharField()
    # intermediaire = forms.CharField()
    # short_description = forms.CharField()
    # image = forms.ImageField()
    # coassurance = forms.BooleanField()
    # operation_adresse = forms.CharField()
    # operation_description = forms.Textarea()
    # price_operation = forms.DecimalField()
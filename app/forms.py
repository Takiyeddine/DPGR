from django import forms
from .models import Projet
 
class Projet_Form(forms.ModelForm):
  class Meta:
    model = Projet
    fields = ["type", "nom","etat_avencement","etat_projet","phase"]
    labels = {'type': "type", 'nom': "nom",'etat_avencement': "etat_avencement",'etat_projet': "etat_projet",'phase': "phase",}
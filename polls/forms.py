from django import forms
from django.forms import ModelForm
from .models import DemandeCapture

# Formulaire Connexion
class Connexion(forms.Form):
    user_id = forms.CharField(label="Identifiant",widget=forms.TextInput(attrs={"class":"form-control",'required':True}))
    user_pwd = forms.CharField(label="Mot de passe",widget=forms.PasswordInput(attrs={"class":"form-control",'required':True}))

# Formulaire demande de capture
class DemandeCaptureForm(ModelForm):
    class Meta:
        model = DemandeCapture
        fields = ["nom_demande","interface_reseau","Nbr_paquet","Filtre"]
        widgets = {
            "Nbr_paquet": forms.NumberInput()
        }
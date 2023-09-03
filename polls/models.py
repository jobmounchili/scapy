from django.db import models
from scapy.all import *
from scapy.config import conf
from django.contrib.auth.models import User

for i in User.objects.all():
    print(i.id)
list_iface = []
id = 1
for i in get_if_list():
    one_set = (str(id),i)
    list_iface.append(one_set)
    id = id + 1
print(list_iface)

# Create your models here.

#Model Demande de capture
class DemandeCapture(models.Model):
    id_dc = models.BigAutoField(primary_key=True)
    nom_demande = models.CharField(max_length=200,blank=True)
    interface_reseau = models.CharField(max_length=200,blank=True,choices=list_iface)
    Nbr_paquet = models.CharField(max_length=200,blank=True)
    Filtre = models.CharField(max_length=200,blank=True, null=True)
    etat = models.IntegerField(blank=True, null=True, default=1)
    id = models.ForeignKey(User, on_delete = models.CASCADE, db_column="id",null=True)

# Model Capture
class Capture(models.Model):
    id_c = models.BigAutoField(primary_key=True)
    capture_data = models.TextField(blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True,blank=True, null=True)
    id_dc = models.ForeignKey("DemandeCapture", on_delete = models.CASCADE, db_column="id_dc")
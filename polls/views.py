from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.template import loader
from .forms import DemandeCaptureForm
from .models import DemandeCapture, Capture
from .forms import Connexion
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from scapy.all import *
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
# Create your views here.

# user = User.objects.create_user(username="jean",password="azerty456")
# user.save()

def connexion(request):
    connect = Connexion()
    if request.method == 'POST':
        connect = Connexion(request.POST)
        if connect.is_valid():
            # user = connect.login(request)
            nom = request.POST.get("user_id")
            pwd = request.POST.get("user_pwd")
            user = authenticate(request,username=nom,password=pwd)
            if user is not None:
                login(request, user)
                print (nom+" "+pwd)
                messages.warning(request, "Bienvenue "+str(request.user)+" !")
                return redirect("./demandeCapture")
            else :
                messages.warning(request, 'Identifiant ou mot de passe incorrecte❌')
        else:
            connect = Connexion()
    context = {
        "form1":connect
    }
    return render(request,"polls/connexion.html",context)

@csrf_protect
@login_required(login_url="connexion")
def index(request):
    all_demande = DemandeCapture.objects.all().values_list()
    print(all_demande)
    form1 = DemandeCaptureForm()
    if request.method == "POST":
        form1 = DemandeCaptureForm(request.POST)
        if form1.is_valid():
            all_demande = DemandeCapture.objects.all().values_list()
            nom_demande = request.POST.get("nom_demande")
            for i in all_demande:
                # Vérifier s'il existe une demande avec ce nom
                if nom_demande == i[1]:
                    messages.success(request,'Il existe une demande avec ce nom⚠️')
                    return redirect("./demandeCapture")
            DemandeCapture.objects.create(nom_demande=request.POST["nom_demande"],interface_reseau=request.POST["interface_reseau"],Nbr_paquet=request.POST["Nbr_paquet"],Filtre=request.POST["Filtre"]).save()
            messages.success(request,'Demande envoyée✅')
            print("Demande créée !")
            return redirect("./demandeCapture")
            # return HttpResponse("Merci")
    context = {
        "form1":form1
    }
    return render(request,"polls/index.html",context)

@csrf_protect
@login_required(login_url="connexion")
def interface_capture(request):
    # Si l'utilsateur est expert
    if request.user.is_superuser:
        query = DemandeCapture.objects.all().values()
        print(query)
        if request.method == "POST":
            if request.POST.get("lance_capture"):
                # Lancer une capture
                all_data = []
                dc_id = request.POST["lance_capture"]
                query1 = DemandeCapture.objects.get(id_dc=dc_id )
                cap = sniff(iface=dev_from_index(int(query1.interface_reseau)), count=int(query1.Nbr_paquet), filter=query1.Filtre)
                for i in cap:
                    all_data.append(i[1])
                    print(i[1])
                print(all_data)
                for j in all_data:
                    with open("./polls/capture/"+query1.nom_demande.replace(" ","")+".cap","a") as fichier:
                        fichier.write(str(j)+"\n")
                Capture.objects.create(capture_data=all_data, id_dc=query1)
                # Changer l'état de la demande de capture
                query1.etat = 2
                query1.save()
                messages.success(request,'La capture est lancée✅')
            elif request.POST.get("annule_capture"):
                # Annuler/refuser une demande de capture
                dc_id = request.POST["annule_capture"]
                query1 = DemandeCapture.objects.get(id_dc=dc_id)
                # Changer l'état de la demande de capture
                query1.etat = 0
                query1.save()
                messages.success(request,'Demande de capture annulée✅')
            elif request.POST.get("sup_capture"):
                # Supprimer une demande de capture
                dc_id = request.POST["sup_capture"]
                DemandeCapture.objects.get(id_dc=dc_id).delete()
                messages.success(request,'Demande de capture supprimée✅')
        context = {
            "all_cap":query
        }
        return render(request,"polls/demandecapture.html",context)
    else:
        messages.success(request,'Accès interdit❌')
        return redirect("./demandeCapture")

@csrf_protect
@login_required(login_url="connexion")
def affiche_capture(request):
    #Récuperer toutes les captures effectuées
    all_capture = Capture.objects.all()
    dic_capture = []
    for i in all_capture:
        dic_capture.append({"nom":i.id_dc.nom_demande,"date":i.timestamp,"data":i.capture_data,"id":i.id_c})
    print(dic_capture)
    if request.method == "POST":
        # Suprrimer une capture
        if request.POST.get("sup_capture"):
            c_id =request.POST["sup_capture"]
            Capture.objects.get(id_c= c_id).delete()
            messages.success(request,'Capture supprimée✅')
            return redirect("./afficheCapture")
    context = {
        "all_cap":dic_capture
    }
    return render(request,"polls/capture.html",context)

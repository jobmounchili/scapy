from django.urls import path

from . import views

urlpatterns = [
        path("connexion", views.connexion, name="connexion"),
        path("demandeCapture", views.index, name="index"),
        path("faireCapture", views.interface_capture, name="fcapture"),
        path("afficheCapture", views.affiche_capture, name="acapture")
]

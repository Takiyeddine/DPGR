from django.shortcuts import render
from rest_framework import viewsets
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.shortcuts import render


# Create your views here.
from django.views.generic import ListView
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from app.models import Projet,Phase,Soumissin,Utilisateur,Compte
from app.serializers import PhaseSerializer,ProjeteSerializer, SoumissionSerializer,UtilisateurSerializer,CompteSerializer


from .models import Projet
from .forms import Projet_Form


def indexpage(request):
    return render(request,"acueil.html")

def connexion(request):
    return render(request,"index.html")

def AdminCompte(request):
    return render(request,"admin-compte-user.html")

def AdminPub(request):
    return render(request,"admin-publication.html")

def statistique(request):
    return render(request,"statistique_projet.html")

def Projet_form(request):
        if request.method == "POST":
            form = Projet_Form(request.POST)
            if form.is_valid():
              form.save()
        else:
            form = Projet_Form()
        return render(request, 'Projet_form.html', {'form': form})


class AdminProjetList(ListView):
    queryset = Projet.objects.all()
    template_name="admin-projet.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["projets"] = Projet.objects.all()
        context["membres_list"]=Utilisateur.objects.all()
        return context


    


class ProjetViewSet(viewsets.ModelViewSet):
    queryset = Projet.objects.all()
    serializer_class = ProjeteSerializer
    permission_classes = (IsAuthenticated,)

class PhaseViewSet(viewsets.ModelViewSet):
    queryset = Phase.objects.all()
    serializer_class = PhaseSerializer
    permission_classes = (IsAuthenticated,)

class SoumissionViewSet(viewsets.ModelViewSet):
    queryset = Soumissin.objects.all()
    serializer_class = SoumissionSerializer
    permission_classes = (IsAuthenticated,)

class UtilisateurViewSet(viewsets.ModelViewSet):
    queryset = Utilisateur.objects.all()
    serializer_class = UtilisateurSerializer
    permission_classes = (IsAuthenticated,)

class CompteViewSet(viewsets.ModelViewSet):
    queryset = Compte.objects.all()
    serializer_class = CompteSerializer
    permission_classes = (IsAuthenticated,)
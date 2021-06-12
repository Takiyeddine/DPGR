from django.contrib import admin

# Register your models here.
from app.models import Projet,Phase,Soumissin,Utilisateur,Compte

class PhaseInLine(admin.TabularInline):
    model=Phase

@admin.register(Phase,Soumissin,Compte)
class GenericAdmin(admin.ModelAdmin):
    pass

@admin.register(Utilisateur)
class UtilisateurtAdmin(admin.ModelAdmin):
    list_display = ('nom','type_util')

@admin.register(Projet)
class ProjettAdmin(admin.ModelAdmin):
    list_display = ('type','nom','etat_avencement','etat_projet')
    #inlines = ('PhaseInLine')
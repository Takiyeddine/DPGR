from django.db import models

# Create your models here.
from django.forms import CharField



class Projet(models.Model):
    type =models.CharField(max_length=255)
    nom = models.CharField(max_length=255)
    etat_avencement = models.CharField(max_length=255)
    etat_projet = models.CharField(max_length=255)

    #=models.ManyToManyField(Utilisateur)
    phase=models.ForeignKey('Phase',null=True,on_delete=models.CASCADE)

    def __str__(self):
        return self.nom

class Utilisateur(models.Model):
    nom=models.CharField(max_length=255)
    prenom=models.CharField(max_length=255)
    type_util=models.CharField(max_length=255)
    projet = models.ForeignKey('Projet', null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.nom+' '+self.prenom

class Phase (models.Model):
    date_debut=models.DateField()
    date_fin=models.DateField()
    description = models.CharField(max_length=255)

    def __str__(self):
        return self.description

class Soumissin(models.Model):
    date=models.DateField()
    etat=models.BooleanField()

    Nom_projet=models.ForeignKey('Projet',null=False,on_delete=models.CASCADE)
    qui_soumit=models.ForeignKey('Utilisateur',null=True,on_delete=models.CASCADE)



class Compte(models.Model):
    adress_mail=models.CharField(max_length=255)
    mot_de_passe=models.CharField(max_length=255)

    utilisateur=models.ForeignKey('Utilisateur',null=False,on_delete=models.CASCADE)
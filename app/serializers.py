from rest_framework import serializers

from app.models import Projet, Phase, Soumissin,Utilisateur,Compte


class ProjeteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Projet
        fields = '__all__'


class PhaseSerializer(serializers.ModelSerializer):
    class Meta:
        model=Phase
        fields = '__all__'

class SoumissionSerializer(serializers.ModelSerializer):
    class Meta:
        model=Soumissin
        fields = '__all__'

class UtilisateurSerializer(serializers.ModelSerializer):
    Fonction =serializers.CharField(source='type_util')
    class Meta:
        model=Utilisateur
        exclude=['type_util']

class CompteSerializer(serializers.ModelSerializer):
    class Meta:
        model=Compte
        fields = '__all__'
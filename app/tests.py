from django.test import TestCase

from app.models import Utilisateur


class AppTestCase(TestCase):
    def test_create_Utilisateur(self):
        nbr_of_user_before_add= Utilisateur.objects.count()
        new_Utilisateur= Utilisateur()
        new_Utilisateur.nom='Amoura'
        new_Utilisateur.prenom='Zahra'
        new_Utilisateur.type_util='Dortorant'
        new_Utilisateur.save()
        nbr_of_user_after_add= Utilisateur.objects.count()
        self.assertTrue(nbr_of_user_after_add == nbr_of_user_before_add+1)
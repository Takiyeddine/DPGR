from rest_framework import routers
from django.conf.urls import url
from . import views
from django.urls import path
from app.views import ProjetViewSet, PhaseViewSet, CompteViewSet, UtilisateurViewSet, SoumissionViewSet, \
    AdminProjetList, AdminCompte,AdminPub,statistique
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns=[
    path('', views.indexpage, name='index'),
    path('connexion', views.connexion, name='connexion'),
    path('statististique',views.statistique,name='statistique'),
    path('publication',views.AdminPub,name='publication'),
    path('comptes',views.AdminCompte,name='comptes'),
    path('admin-projet',views.AdminProjetList.as_view(),name='admin-projet'),
    url('form', views.Projet_form, name='form')
    #path('',AdminProjetList.as_view(),name="projet"),
    #path('',UtilisateurView.as_view(),name="membre")
]

urlpatterns += staticfiles_urlpatterns()
router = routers.DefaultRouter()
router.register('projet',ProjetViewSet)
router.register('phase',PhaseViewSet)
router.register('soumission',SoumissionViewSet)
router.register('utilisateur',UtilisateurViewSet)
router.register('compte',CompteViewSet)

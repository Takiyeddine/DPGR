# Generated by Django 3.2.4 on 2021-06-08 20:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Phase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_debut', models.DateField()),
                ('date_fin', models.DateField()),
                ('description', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Projet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=255)),
                ('nom', models.CharField(max_length=255)),
                ('etat_avencement', models.CharField(max_length=255)),
                ('etat_projet', models.CharField(max_length=255)),
                ('phase', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.phase')),
            ],
        ),
        migrations.CreateModel(
            name='Utilisateur',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=255)),
                ('penom', models.CharField(max_length=255)),
                ('type_util', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Soumissin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('etat', models.CharField(max_length=255)),
                ('Nom_projet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.projet')),
                ('qui_soumit', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.utilisateur')),
            ],
        ),
        migrations.CreateModel(
            name='Compte',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('adress_mail', models.CharField(max_length=255)),
                ('mot_de_passe', models.CharField(max_length=255)),
                ('utilisateur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.utilisateur')),
            ],
        ),
    ]

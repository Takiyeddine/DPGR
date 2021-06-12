# Generated by Django 3.2.4 on 2021-06-11 19:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_projet_membre'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='projet',
            name='membre',
        ),
        migrations.AddField(
            model_name='utilisateur',
            name='projet',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.projet'),
        ),
    ]

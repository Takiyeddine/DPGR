# Generated by Django 3.2.4 on 2021-06-11 15:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_alter_soumissin_etat'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projet',
            name='phase',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.phase'),
        ),
    ]

# Generated by Django 3.2.7 on 2022-01-08 15:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0004_mtmprofile'),
        ('made_to_measure', '0005_auto_20211227_1208'),
    ]

    operations = [
        migrations.AddField(
            model_name='mtmorder',
            name='user_profile',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='mtm_orders', to='profiles.mtmprofile'),
        ),
    ]

# Generated by Django 4.2.9 on 2024-07-29 20:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0014_remove_hero_cv'),
    ]

    operations = [
        migrations.AddField(
            model_name='hero',
            name='cv',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.cv'),
        ),
    ]

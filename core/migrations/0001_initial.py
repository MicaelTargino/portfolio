# Generated by Django 4.2.14 on 2024-07-25 23:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Style',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('primary_color', models.CharField(blank=True, max_length=8, null=True)),
                ('secondary_color', models.CharField(blank=True, max_length=8, null=True)),
                ('terciary_color', models.CharField(blank=True, max_length=8, null=True)),
                ('dark_mode', models.BooleanField(default=True)),
                ('white', models.CharField(blank=True, default='#fff', max_length=8, null=True)),
                ('logo', models.FileField(blank=True, null=True, upload_to='')),
                ('favicon', models.FileField(blank=True, null=True, upload_to='')),
                ('hero_image', models.FileField(blank=True, null=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Hero',
            fields=[
                ('section', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='core.section')),
                ('labels', models.CharField(default='Programmer', max_length=255)),
                ('slogan', models.CharField(max_length=512)),
                ('cv', models.ImageField(upload_to='cv/')),
                ('link_to_section', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='professionals', to='core.section')),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.user')),
            ],
        ),
    ]

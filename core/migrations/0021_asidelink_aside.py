# Generated by Django 4.2.9 on 2024-07-29 21:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0020_delete_aside'),
    ]

    operations = [
        migrations.CreateModel(
            name='AsideLink',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('section', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='aside_link_to_section', to='core.section')),
            ],
        ),
        migrations.CreateModel(
            name='Aside',
            fields=[
                ('section', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='core.section')),
                ('name', models.CharField(blank=True, max_length=25, null=True)),
                ('links', models.ManyToManyField(blank=True, to='core.asidelink')),
            ],
        ),
    ]
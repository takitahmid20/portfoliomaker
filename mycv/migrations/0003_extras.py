# Generated by Django 3.2.8 on 2021-12-17 14:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mycv', '0002_languageskills_myskills'),
    ]

    operations = [
        migrations.CreateModel(
            name='extras',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_completed_projects', models.IntegerField(blank=True, null=True)),
                ('total_clients', models.IntegerField(blank=True, null=True)),
                ('owner', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='mycv.profile')),
            ],
        ),
    ]
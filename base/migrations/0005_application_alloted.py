# Generated by Django 4.1.3 on 2022-11-22 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_slots_company_name_alter_application_applied'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='alloted',
            field=models.BooleanField(default=False),
        ),
    ]

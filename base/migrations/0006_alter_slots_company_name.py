# Generated by Django 4.1.3 on 2022-11-22 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0005_application_alloted'),
    ]

    operations = [
        migrations.AlterField(
            model_name='slots',
            name='company_name',
            field=models.CharField(default='', max_length=50, null=True),
        ),
    ]
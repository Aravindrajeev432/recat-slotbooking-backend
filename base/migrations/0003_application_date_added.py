# Generated by Django 4.1.3 on 2022-11-20 17:19

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_application_proposal_application_state_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='date_added',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]

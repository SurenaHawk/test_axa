# Generated by Django 4.2.11 on 2024-05-07 12:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contrat', '0010_projet_image_plan_opeation_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='projet',
            old_name='image_plan_opeation',
            new_name='image_plan_operation',
        ),
    ]

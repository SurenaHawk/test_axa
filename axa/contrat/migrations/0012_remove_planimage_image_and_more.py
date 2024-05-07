# Generated by Django 4.2.11 on 2024-05-07 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contrat', '0011_rename_image_plan_opeation_projet_image_plan_operation'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='planimage',
            name='image',
        ),
        migrations.RemoveField(
            model_name='projet',
            name='image_plan_operation',
        ),
        migrations.AddField(
            model_name='planimage',
            name='image_plan_operation',
            field=models.ImageField(blank=True, null=True, upload_to='images_plan/'),
        ),
    ]
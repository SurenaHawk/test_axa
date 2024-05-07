# Generated by Django 4.2.11 on 2024-05-07 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contrat', '0009_projet_docx_file_projet_pdf_file_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='projet',
            name='image_plan_opeation',
            field=models.ImageField(blank=True, null=True, upload_to='images_plan'),
        ),
        migrations.AlterField(
            model_name='projet',
            name='opportunity_number',
            field=models.IntegerField(unique=True, verbose_name="Numéro d'opportunité"),
        ),
    ]

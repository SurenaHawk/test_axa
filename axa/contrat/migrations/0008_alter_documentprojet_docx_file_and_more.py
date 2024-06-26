# Generated by Django 4.2.11 on 2024-05-06 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contrat', '0007_alter_documentprojet_docx_file_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='documentprojet',
            name='docx_file',
            field=models.FileField(blank=True, null=True, upload_to='docx_files/'),
        ),
        migrations.AlterField(
            model_name='documentprojet',
            name='pdf_file',
            field=models.FileField(blank=True, null=True, upload_to='pdf_files/'),
        ),
    ]

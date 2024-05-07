# Generated by Django 4.2.11 on 2024-05-06 13:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contrat', '0004_planimage'),
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pdf_file', models.BinaryField(blank=True, null=True)),
                ('docx_file', models.BinaryField(blank=True, null=True)),
                ('projet', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='contrat.projet')),
            ],
        ),
    ]

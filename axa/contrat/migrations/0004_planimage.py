# Generated by Django 4.2.11 on 2024-05-05 19:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contrat', '0003_alter_projet_operation_description_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='PlanImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('projet', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='contrat.projet')),
            ],
        ),
    ]

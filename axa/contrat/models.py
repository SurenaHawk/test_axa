from django.db import models
from ckeditor.fields import RichTextField
from multiupload.fields import MultiImageField

# Create your models here.

class Projet(models.Model):
    opportunity_number = models.IntegerField(verbose_name="Numéro d'opportunité")
    client_name = models.CharField(max_length=255)
    siret_number = models.IntegerField(verbose_name="Numéro SIRET", blank=True, null=True)
    siren_number = models.IntegerField(verbose_name="Numéro SIREN", blank=True, null=True)
    affaire = models.CharField(max_length=100)
    reference = models.CharField(max_length=10)
    intermediaire = models.CharField(max_length=255)
    short_description = models.CharField(verbose_name="Courte description",max_length=255)
    image = models.ImageField(upload_to="images/", blank=True, null=True)
    coassurance = models.BooleanField(default=False)
    operation_adresse = models.CharField(max_length=255)
    operation_description = RichTextField()
    price_operation = models.DecimalField(max_digits=8, decimal_places=2)
    pdf_file = models.FileField(upload_to='pdf_files/', null=True, blank=True)
    docx_file = models.FileField(upload_to='docx_files/', null=True, blank=True)

    def __str__(self):
        return self.reference

class PlanImage(models.Model):
    projet = models.ForeignKey(Projet, on_delete=models.PROTECT)
    image = models.ImageField(null=True, blank=True)


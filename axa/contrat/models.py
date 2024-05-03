from django.db import models

# Create your models here.

class Projet(models.Model):
    opportunity_number = models.IntegerField(verbose_name="Numéro d'opportunité")
    client_name = models.CharField(max_length=255)
    siret_number = models.IntegerField(verbose_name="Numéro SIRET", blank=True, null=True)
    siren_number = models.IntegerField(verbose_name="Numéro SIREN", blank=True, null=True)
    affaire = models.CharField(max_length=100)
    reference = models.CharField(max_length=10)
    intermediaire = models.CharField(max_length=255)
    short_description = models.TextField(verbose_name="Courte description")
    image = models.ImageField(upload_to="images/", blank=True, null=True)
    coassurance = models.BooleanField(default=False)
    operation_adresse = models.CharField(max_length=255)
    operation_description = models.TextField()
    price_operation = models.DecimalField(max_digits=8, decimal_places=2)


    def __str__(self):
        return self.opportunity_number+" "+self.reference



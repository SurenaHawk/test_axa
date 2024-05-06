from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Projet, PlanImage
# Create your views here.

def home(request):
    return render(request, 'contrat/home.html')

@csrf_exempt    
def devis(request):
    if request.method == 'POST':
        opportunity_number = request.POST.get("opportunity_number")
        client_name = request.POST.get("client_name")
        siret_number = request.POST.get("siret_number")
        siren_number = request.POST.get("siren_number")
        affaire = request.POST.get("affaire")
        reference = request.POST.get("reference")
        intermediaire = request.POST.get("intermediaire")
        short_description = request.POST.get("short_description")
        image_description = request.FILES.get("image_description")
        coassurance = request.POST.get("coassurance")
        operation_adresse = request.POST.get("operation_adresse")
        plan_operation = request.FILES.getlist("plan_operation")
        operation_description = request.POST.get("operation_adresse")
        tarif = request.POST.get('tarif')

        if (
            opportunity_number is not None and client_name is not None and siret_number is not None and siren_number is not None and affaire is not None 
            and reference is not None and intermediaire is not None and short_description is not None and image_description is not None and coassurance is not None 
            and operation_adresse is not None and plan_operation is not None and operation_description is not None and tarif is not None
        ):
            coassurance_field = False
            if coassurance == "True":
                coassurance_field = True
            projet = Projet.objects.create(
                opportunity_number = opportunity_number,
                client_name = client_name,
                siret_number = siret_number,
                siren_number = siret_number,
                affaire = affaire,
                reference = reference,
                intermediaire = intermediaire,
                short_description = short_description,
                image = image_description,
                coassurance = coassurance_field,
                operation_adresse = operation_adresse,
                operation_description = operation_description,
                price_operation = tarif
            )

            projet.save()
        return redirect(reverse('home'))
    else:
        message_danger = "Une erreur est survenue lors de la création du devis"
        #return render(request, "contrat/devis.html", {"message_danger":message_danger})
    return render(request, 'contrat/devis.html')



from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Projet, PlanImage
from io import BytesIO
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from docx import Document
from django.conf import settings
import os
from django.core.files.base import ContentFile
from datetime import datetime
from django.core.files.storage import default_storage
from PIL import Image
import io
from tempfile import NamedTemporaryFile
import tempfile


# Create your views here.

def home(request):
    projets = Projet.objects.all()
    return render(request, 'contrat/home.html', {'projets': projets})

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
        image = request.FILES.get("image_description")
        coassurance = request.POST.get("coassurance")
        operation_adresse = request.POST.get("operation_adresse")
        plan_operation = request.FILES.getlist("plan_operation")
        operation_description = request.POST.get("operation_adresse")
        price_operation = request.POST.get('tarif')

        if (
            opportunity_number is not None and client_name is not None and siret_number is not None and siren_number is not None and affaire is not None 
            and reference is not None and intermediaire is not None and short_description is not None and image is not None and coassurance is not None 
            and operation_adresse is not None and plan_operation is not None and operation_description is not None and price_operation is not None
        ):
            coassurance_field = False
            if coassurance == "True":
                coassurance_field = True
            projet = Projet.objects.create(
                opportunity_number = opportunity_number,
                client_name = client_name,
                siret_number = siret_number,
                siren_number = siren_number,
                affaire = affaire,
                reference = reference,
                intermediaire = intermediaire,
                short_description = short_description,
                image = image,
                coassurance = coassurance_field,
                operation_adresse = operation_adresse,
                operation_description = operation_description,
                price_operation = price_operation
            )

            projet.save()

            data = [
                opportunity_number, client_name, siret_number, siren_number, affaire, reference, intermediaire, short_description, 
                image, coassurance, operation_adresse, operation_description, price_operation
            ]

            pdf_content = generate_pdf(data)
            docx_content = generate_docx(data)
            projet.pdf_file.save('Projet_de_contrat_'+opportunity_number+'_Date_'+datetime.now().strftime('%Y-%m-%d_%H-%M-%S')+'.pdf', ContentFile(pdf_content))
            projet.docx_file.save('Projet_de_contrat_'+opportunity_number+'_Date_'+datetime.now().strftime('%Y-%m-%d_%H-%M-%S')+'.docx', ContentFile(docx_content))

            return HttpResponse("Fichiers générés et enregistrés avec succès.")


    else:
        return render(request, 'contrat/devis.html')
        #message_danger = "Une erreur est survenue lors de la création du devis"
        #return render(request, "contrat/devis.html", {"message_danger":message_danger})
    return render(request, 'contrat/devis.html')

def generate_pdf(data):
    buffer = BytesIO()
    p = canvas.Canvas(buffer, pagesize=letter)
    
    left_margin = 50
    top_margin = 620

    p.drawImage("https://upload.wikimedia.org/wikipedia/commons/thumb/9/94/AXA_Logo.svg/1200px-AXA_Logo.svg.png", left_margin, top_margin, 100,80)
    
    p.setFont("Helvetica-Bold", 14)
    devis_width = p.stringWidth("Devis", "Helvetica-Bold")
    p.drawString(letter[0] - left_margin - devis_width, 750, "Devis")

    p.setFont("Helvetica-Bold", 10)
    p.drawString(50, 620 - 40 - 20, "Numéro opportunité : {}".format(data[0]))
    p.drawString(50, 620 - 40 - 40, "Référence : {}".format(data[5]))
    p.drawString(50, 620 - 40 - 60, "Nom client : {}".format(data[1]))
    p.drawString(50, 620 - 40 - 80, "Intermédiaire : {}".format(data[6]))
    p.drawString(50, 620 - 40 - 100, "Description succinte : {}".format(data[7]))


    # image_content = data[8].read()
    # print("image_content", image_content)
    # image_pil = Image.open(image_content)
    # print("image_pil", image_pil)

    # print("data", data[8])
    # print(type(data[8]))
    # instance_image = Image.open(BytesIO(data[8].read()), formats=['JPEG'])
    # print("instance", instance_image)
    # p.drawImage(instance_image, left_margin, top_margin, width=100, height=100)

    # p.setFont("Helvetica-Bold", 10)
    # p.drawString(left_margin, top_margin - 40 - 20, "Numéro opportunité:")
    # p.drawString(left_margin, top_margin - 40 - 40, "Référence:")
    # p.drawString(left_margin, top_margin - 40 - 60, "Nom Client:")
    # p.drawString(left_margin, top_margin - 40 - 80, "Intermédiaire:")
    # p.drawString(left_margin, top_margin - 40 - 100, "Description succinte:")
    # p.drawString(left_margin, top_margin - 40 - 120, "Image correspondant à la description :")

    
    # p.setFont("Helvetica", 10)
    # p.drawString(left_margin + 103, top_margin - 40 - 20, str(data[0]))
    # p.drawString(left_margin + 57, top_margin - 40 - 40, str(data[5]))
    # p.drawString(left_margin + 60, top_margin - 40 - 60, str(data[1]))
    # p.drawString(left_margin + 60, top_margin - 40 - 80, str(data[6]))
    # p.drawString(left_margin + 60, top_margin - 40 - 100, str(data[7]))

    # temp_image_path = default_storage.save('temp_instance_image.png', ContentFile(data[8].read()))
    # p.drawImage(temp_image_path, left_margin, top_margin - 50 - 60 - 100, width=100, height=100)

    p.showPage()
    p.save()
    pdf_content = buffer.getvalue()
    buffer.close()
    return pdf_content

def generate_docx(data):
    doc = Document()
    doc.add_heading('Informations', level=1)
    doc.add_paragraph("Nom: test")
    # Ajoutez d'autres informations du modèle au DOCX si nécessaire
    temp_path = os.path.join(settings.MEDIA_ROOT, 'temp.docx')
    doc.save(temp_path)
    with open(temp_path, 'rb') as f:
        docx_content = f.read()
    os.remove(temp_path)
    return docx_content


def download_pdf(request):
    opportunity_number = request.GET.get('opportunity_number')
    projets = Projet.objects.filter(opportunity_number=opportunity_number)
    for projet in projets:
        pdf_document = projet.pdf_file
        response = HttpResponse(pdf_document, content_type='application/pdf')
        response['Content-Disposition'] = f'attachment; filename="Projet_de_contrat_'+opportunity_number+'_Date_'+datetime.now().strftime('%Y-%m-%d_%H-%M-%S')+'.pdf'
    return response

def download_docx(request):
    opportunity_number = request.GET.get('opportunity_number')
    projets = Projet.objects.filter(opportunity_number=opportunity_number)
    for projet in projets:
        pdf_document = projet.docx_file
        response = HttpResponse(pdf_document, content_type='application/docx')
        response['Content-Disposition'] = f'attachment; filename="Projet_de_contrat_'+opportunity_number+'_Date_'+datetime.now().strftime('%Y-%m-%d_%H-%M-%S')+'.docx'
    return response

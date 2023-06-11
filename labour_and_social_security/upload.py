from .models import *

def handle_uploaded_file(file):
    new_document = Work_Permit(pdf=file)
    new_document.save()

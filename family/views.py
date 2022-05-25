from multiprocessing import context
from django.shortcuts import render
from family.models import Registro

def registro(request):
    family_new = Registro.objects.all()
    context= {"family_new":family_new}
    return render (request, "registro.html", context = context)


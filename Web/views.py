from contextvars import Context
from multiprocessing import context
from pipes import Template
from django.http import HttpResponse
from django.shortcuts import render

def saludo (request,nombre):
        return HttpResponse(f"<h1>Hola {nombre}!</h1>")

def probando_template(request):
        context ={
        "nombre":"Renata",
        "apellido":"Cardoso",
        }
        return render(request,"template.html",context = context)


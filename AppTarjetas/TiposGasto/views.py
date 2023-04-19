from django.shortcuts import render, HttpResponse

# Create your views here.



def hola_Mundo(request):
    return HttpResponse("<h1>Hola Mundo con django<h1/>")

from django.shortcuts import render
from django.http import HttpResponse


def visualizar_home(request):
    return HttpResponse(content="Olá, seja bem vindo")


# Create your views here.

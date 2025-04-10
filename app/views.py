from django.shortcuts import render

from produtos.models import Produtos


def home(request):
    produtos = Produtos.objects.all().filter(esta_disponivel=True)

    context = {"produtos": produtos}

    return render(request, "home.html", context)

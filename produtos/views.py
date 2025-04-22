from django.shortcuts import get_object_or_404, render

from categorias.models import Categorias
from produtos.models import Produtos


def visualizarLoja(request, categoria_slug=None):
    categorias = None
    produtos = None

    if categoria_slug:
        categorias = get_object_or_404(Categorias, slug=categoria_slug)
        produtos = Produtos.objects.filter(categoria=categorias, esta_disponivel=True)
        produtos_quantidade = produtos.count()
    else:
        produtos = Produtos.objects.all().filter(esta_disponivel=True)
        produtos_quantidade = produtos.count()

    context = {
        "produtos": produtos,
        "produtos_quantidade": produtos_quantidade,
    }

    return render(request, "loja/loja.html", context)


def produto_detalhe(request, categoria_slug, produto_slug):
    try:
        produto = Produtos.objects.get(
            categoria__slug=categoria_slug, slug=produto_slug
        )
    except Exception as ex:
        raise ex

    context = {
        "produto": produto,
    }

    return render(request, "loja/produto_detalhe.html", context)

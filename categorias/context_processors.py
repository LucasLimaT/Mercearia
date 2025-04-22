from categorias.models import Categorias


def categorias_menu(request):
    lista_opcoes = Categorias.objects.all()
    return dict(opcoes=lista_opcoes)

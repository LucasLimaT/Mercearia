from django.db import models
from django.urls import reverse
from categorias.models import Categorias


# Create your models here.
class Produtos(models.Model):
    categoria = models.ForeignKey(Categorias, on_delete=models.CASCADE)
    produto_nome = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    descricao = models.TextField(max_length=300, unique=True)
    preco = models.DecimalField(max_digits=12, decimal_places=2)
    imagens = models.ImageField(upload_to="fotos/produtos/")
    estoque = models.IntegerField()
    esta_disponivel = models.BooleanField(default=True)
    criado_em = models.DateTimeField(auto_now_add=True)
    modificado_em = models.DateTimeField(auto_now=True)


def get_url(self):
    return reverse("produto_detalhe", args=[self.categoria.slug, self.slug])

from django.db import models
from django.urls import reverse


# Create your models here.
class Categorias(models.Model):
    categorias_nome = models.CharField(max_length=80, unique=True)
    slug = models.SlugField(max_length=100, unique=True, null=True)
    categoria_descricao = models.TextField(max_length=255, blank=True)
    categoria_imagem = models.ImageField(upload_to="fotos/categorias/", blank=True)


def __str__(self):
    return self.categorias_nome


def get_url(self):
    return reverse("produtos_por_categoria", args=[self.slug])

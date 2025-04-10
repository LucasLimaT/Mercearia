from django.contrib import admin
from categorias.models import Categorias


# Register your models here.
class CategoriaAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("categorias_nome",)}
    list_display = ("categorias_nome", "slug")


admin.site.register(Categorias, CategoriaAdmin)

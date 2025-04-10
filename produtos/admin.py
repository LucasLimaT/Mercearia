from django.contrib import admin

from produtos.models import Produtos


class ProdutosAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        "slug": (
            "produto_nome",
            "preco",
            "slug",
            "estoque",
            "esta_disponivel",
        )
    }
    list_display = (
        "produto_nome",
        "slug",
    )


admin.site.register(Produtos, ProdutosAdmin)

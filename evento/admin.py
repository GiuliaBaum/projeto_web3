
# evento/admin.py
from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html
from .models import Evento, Post
from insumo.models import Insumo
from voluntario.models import Voluntario
from core.admin import ExportPdfMixin

# cabeçalhos gerais
admin.site.site_header  = "Sistema de Administração FFC"
admin.site.site_title   = "Administração"
admin.site.index_title  = "Painel de Controle"

@admin.register(Evento)
class EventoAdmin(ExportPdfMixin, admin.ModelAdmin):
    list_display      = ('nome', 'descricao', 'data', 'acoes')
    list_display_links= ('nome',)
    search_fields     = ("nome", "gerente__nome")

    def acoes(self, obj):
        delete_url = reverse(
            f'admin:{obj._meta.app_label}_{obj._meta.model_name}_delete',
            args=[obj.pk]
        )
        pdf_url = reverse(
            f'admin:{obj._meta.app_label}_{obj._meta.model_name}_export_pdf',
            args=[obj.pk]
        )
        return format_html(
            '<a href="{}" class="deletelink">Excluir</a> '
            '<a href="{}" class="pdflink" title="Gerar PDF">🖨️ Gerar PDF</a>',
            delete_url, pdf_url
        )
    acoes.short_description = 'Ações'


@admin.register(Post)
class PostAdmin(ExportPdfMixin, admin.ModelAdmin):
    list_display      = ('titulo', 'legenda', 'acoes')
    list_display_links= ('titulo',)
    search_fields     = ("titulo",)

    def acoes(self, obj):
        delete_url = reverse(
            f'admin:{obj._meta.app_label}_{obj._meta.model_name}_delete',
            args=[obj.pk]
        )
        pdf_url = reverse(
            f'admin:{obj._meta.app_label}_{obj._meta.model_name}_export_pdf',
            args=[obj.pk]
        )
        return format_html(
            '<a href="{}" class="deletelink" title="Excluir">×</a> '
            '<a href="{}" class="deletelink" title="Gerar PDF">🖨️</a>',
            delete_url, pdf_url
        )
    acoes.short_description = 'Ações'
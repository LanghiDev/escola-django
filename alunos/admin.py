from django.contrib import admin
from alunos.models import Aluno

# Register your models here.
class AlunoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'serie', 'media_final')
    list_filter = ('usuario', 'media_final',)

admin.site.register(Aluno, AlunoAdmin)
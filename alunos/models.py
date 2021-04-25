from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Aluno(models.Model):
    nome = models.CharField(max_length=60)
    serie = models.SmallIntegerField()
    media1 = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    media2 = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    media3 = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    media4 = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    media_final = models.CharField(max_length=10, blank=True, null=True)
    data_criacao = models.DateTimeField(auto_now=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = 'aluno'

    def __str__(self):
        return self.nome

from django.db import models
from datetime import datetime


# informações (campos) que serão solicitados ao usuário no cadastro
class Vouchers(models.Model):
    nome = models.CharField(max_length=100)
    tel = models.CharField(max_length=15)
    voucher = models.CharField(max_length=10, null=True)
    dataCadastro = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.nome
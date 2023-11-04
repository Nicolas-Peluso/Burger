from django.db import models

class Pedidos(models.Model):
    NomeCliente = models.TextField(max_length=150);
    SenhaCliente = models.TextField(max_length=150);

def __str__(self):
    return f"Fototgrafia [nome={self.NomeCliente}]"
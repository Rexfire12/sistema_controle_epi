from django.db import models

# Create your models here.
class Usuario(models.Model):
    nome = models.CharField(max_length=100)
    

    def __str__(self):
        return f"Usuario: {self.nome}"
class Equipamento(models.Model):
        nome = models.CharField(max_length=100)
        ca = models.CharField(max_length=100)
        validade = models.CharField(max_length=100)
        
        
        def __str__(self):
            return f"Equipamento: {self.nome}"
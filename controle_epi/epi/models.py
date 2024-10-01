from django.db import models

# Create your models here.

class Equipamento(models.Model):
        nome = models.CharField(max_length=100)
        ca = models.IntegerField(max_length=100)
        validade = models.TextField(max_length=100)
        
        
        def __str__(self):
            return f"Equipamento: {self.nome, self.ca, self.validade}"
        
class Colaborador(models.Model):
        nome = models.CharField(max_length=100)
        cargo = models.CharField(max_length=100)
        matricula = models.IntegerField(max_length=100)
            
        def __str__(self):
                return f"Colaborador: {self.nome , self.cargo, self.matricula}"
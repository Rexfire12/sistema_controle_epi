from django.db import models

# Create your models here.

class Equipamento(models.Model):
        nome = models.CharField(max_length=100)
        ca = models.IntegerField(max_length=100)
        validade = models.DateField()
        
        
        def __str__(self):
            return f"Equipamento: {self.nome, self.ca, self.validade}"
        
class Colaborador(models.Model):
        nome = models.CharField(max_length=100)
        cargo = models.CharField(max_length=100)
        matricula = models.IntegerField(max_length=100)
            
        def __str__(self):
                return f"Colaborador: {self.nome , self.cargo, self.matricula}"
        
class Registro(models.Model):
        equipamento = models.ForeignKey(Equipamento, on_delete=models.CASCADE)
        colaborador = models.ForeignKey(Colaborador, on_delete=models.CASCADE)
        data_emprestimo = models.DateField()
        previsao_devolucao = models.DateField()	
        status = models.CharField(max_length=100, default='Em Preparação')
        condicoes = models.CharField(max_length=100)
        data_devolucao = models.DateField()
        observacao = models.CharField(max_length=100)
        def __str__(self):
                return f"Registro: {self.equipamento, self.colaborador, self.data_emprestimo, self.previsao_devolucao, self.status, self.condicoes, self.data_devolucao, self.observacao}"
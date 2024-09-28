from django.shortcuts import render, redirect
from epi.models import Equipamento


# Create your views here.
#Listar Usuários
def index(request):
    return render(request, 'epi/index.html')
def listar_epi(request):
    values = Equipamento.objects.all()
    nome = request.Get.get('nome')
    if nome: 
     values = values.filter(nome__contains=nome)
    return render(request, 'epi/globals/listar.html', {'values': values})
   
#Criar EPI
def criar_epi(request):
    nome = None
    if request.method == 'POST':
        nome = request.POST.get('nome')
        ca = request.POST.get('ca')
        validade = request.POST.get('validade')
        if nome and ca and validade:
           Equipamento.objects.create(nome=nome, equipamento=ca, validade=validade)
        print(nome)
    return render(request, 'epi/globals/cadastrar.html', {"ultimo_nome":nome})
   #Deletar 
def deletar_epi(request, id):
    epi = Equipamento.objects.get(id=id)
    epi.delete()
    return redirect(listar_epi)
   #Atualizar 
def atualizar_epi(request, id):
    epi = Equipamento.objects.get(id=id)
    if request.method == 'POST':
        nome = request.POST.get('nome')
        ca = request.POST.get('ca')
        validade = request.POST.get('ca')
        if nome and ca and validade:
            epi.nome = nome
            epi.ca = ca
            epi.validade = validade
            epi.save()
            return redirect(listar_epi)
        else:
            return render(request, 'epi/globals/atualizar.html', {"item":epi, "erro":True})
    return render(request, 'epi/globals/atualizar.html', {"item":epi})

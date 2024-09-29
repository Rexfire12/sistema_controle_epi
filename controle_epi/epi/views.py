from django.shortcuts import render, redirect
from epi.models import Equipamento


# Create your views here.
#Listar Usuários
def index(request):
    return render(request, 'epi/globals/home.html')

#Cadastrar EPI
def cadastrar_epi(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        ca = request.POST.get('ca')
        validade = request.POST.get('validade')
        epi = Equipamento.objects.create(
            nome=nome,
            ca=ca,
            validade=validade
        )
        return render(request, 'epi/globals/cadastrar.html', {'equipamento': epi})
    return render(request, 'epi/globals/cadastrar.html')

#Editar EPI
def atualizar_epi(request, id):
    equipamento = Equipamento.objects.get(id=id)
    if request.method == 'POST':
        nome = request.POST.get('nome')
        ca = request.POST.get('ca')
        validade = request.POST.get('validade')
        if nome and ca and validade:
            equipamento.nome = nome
            equipamento.ca = ca
            equipamento.validade = validade
            equipamento.save()
            return redirect('/atualizar')
        else:
            return render(request, 'epi/globals/atualizar.html', {'equipamento': equipamento, 'error': 'Todos os campos devem ser preenchidos'})
    return render(request, 'epi/globals/atualizar.html', {'equipamento': equipamento})

#Listar EPIs
def listar_epi(request):
    values = Equipamento.objects.all()
    nome = request.GET.get('nome')
    ca = request.GET.get('ca')
    validade = request.GET.get('validade')
    if nome or ca or validade:
        values = values.filter(
            nome__icontains=nome,
            ca__icontains=ca,
            validade__icontains=validade
        )
    return render(request, 'epi/globals/listar.html', {'equipamento': values})
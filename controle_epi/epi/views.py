from django.shortcuts import render, redirect, get_object_or_404
from epi.models import Equipamento, Colaborador


# Create your views here.
def index(request):
    return render(request, 'epi/globals/home.html')

#Listar EPIs
def listar_epi(request):
    values = Equipamento.objects.all()
    nome = request.GET.get('nome')
    ca = request.GET.get('ca')
    validade = request.GET.get('validade')
    if nome:
        values = values.filter(nome__icontains=nome)
    if ca:
        values = values.filter(ca__icontains=ca)
    if validade:
        values = values.filter(validade__icontains=validade)
    return render(request, 'epi/globals/listar.html', {'equipamentos': values})

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
        return render(request, 'epi/globals/cadastrar.html', {'equipamento': epi,'erro': True})
    return render(request, 'epi/globals/cadastrar.html')

#Editar EPI
def atualizar_epi(request, id=0):
    if id == 0:
        if request.method == 'GET' and request.GET.get('nome_item'):
            nome_item = request.GET.get('nome_item')
            itens = Equipamento.objects.filter(nome__icontains=nome_item)
        else:
            itens = Equipamento.objects.all()
        return render(request, 'epi/globals/atualizar.html', {'itens': itens})
    epi = get_object_or_404(Equipamento, id=id)
    if request.method == 'POST':
        nome = request.POST.get('nome')
        ca = request.POST.get('ca')
        validade = request.POST.get('validade')
        if nome and ca and validade:
            epi.nome = nome
            epi.ca = ca
            epi.validade = validade
            epi.save()
            return redirect(atualizar_epi)
        else:
            return render(request, 'epi/globals/atualizar.html', {'equipamento': epi, 'erro': True})
    return render(request, 'epi/globals/atualizar.html', {'equipamento': epi})

#Excluir EPI
def excluir_epi(request, id):
    epi = Equipamento.objects.get(id=id)
    epi.delete()
    return redirect(atualizar_epi)

#Listar Colaboradores
def listar_colaborador(request):
    values = Colaborador.objects.all()
    nome = request.GET.get('nome')
    cargo = request.GET.get('cargo')
    matricula = request.GET.get('matricula')
    if nome:
        values = values.filter(nome__icontains=nome)
    if cargo:
        values = values.filter(cargo__icontains=cargo)
    if matricula:
        values = values.filter(matricula__icontains=matricula)
    return render(request, 'epi/globals/listar_colaborador.html', {'colaboradores': values})

#Cadastrar Colaboradores
def cadastrar_colaborador(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        cargo = request.POST.get('cargo')
        matricula = request.POST.get('matricula')
        colaborador = Colaborador.objects.create(
            nome=nome,
            cargo=cargo,
            matricula=matricula
        )
        return render(request, 'epi/globals/cadastrar_colaborador.html', {'colaborador': colaborador, 'erro': True})
    return render(request, 'epi/globals/cadastrar_colaborador.html')

#Editar Colaboradores
def atualizar_colaborador(request, id=0):
    if id == 0:
        if request.method == 'GET' and request.GET.get('nome_item'):
            nome_item = request.GET.get('nome_item')
            itens = Colaborador.objects.filter(nome__icontains=nome_item)
        else:
            itens = Colaborador.objects.all()
        return render(request, 'epi/globals/atualizar_colaborador.html', {'itens': itens})
    colaborador = get_object_or_404(Colaborador, id=id)
    if request.method == 'POST':
        nome = request.POST.get('nome')
        cargo = request.POST.get('cargo')
        matricula = request.POST.get('matricula')
        if nome and cargo and matricula:
            colaborador.nome = nome
            colaborador.cargo = cargo
            colaborador.matricula = matricula
            colaborador.save()
            return redirect(atualizar_colaborador)
        else:
            return render(request, 'epi/globals/atualizar_colaborador.html', {'colaborador': colaborador, 'erro': True})
    return render(request, 'epi/globals/atualizar_colaborador.html', {'colaborador': colaborador})

#Excluir Colaboradores
def excluir_colaborador(request, id):    
    colaborador = Colaborador.objects.get(id=id)
    colaborador.delete()
    return redirect(atualizar_colaborador)      


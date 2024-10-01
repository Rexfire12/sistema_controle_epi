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
        return render(request, 'epi/globals/cadastrar.html', {'equipamento': epi})
    return render(request, 'epi/globals/cadastrar.html')

#Editar EPI
def atualizar_epi(request, id):
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
            return redirect('listar_epi')  # Certifique-se de que 'listar_epi' é o nome correto da sua URL
        else:
            return render(request, 'epi/globals/atualizar.html', {'equipamento': epi, 'erro': True})
    return render(request, 'epi/globals/atualizar.html', {'equipamento': epi})

#Excluir
def excluir_epi(request, id):
    epi = Equipamento.objects.get(id=id)
    epi.delete()
    return redirect(listar_epi)

#Listar Usuários
def listar_usuarios(request):
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
    return render(request, 'epi/globals/listar_usuario.html', {'usuario': values})

#Cadastrar Usuários
def cadastrar_usuario(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        cargo = request.POST.get('cargo')
        matricula = request.POST.get('matricula')
        usuario = Colaborador.objects.create(
            nome=nome,
            cargo=cargo,
            matricula=matricula
        )
        return render(request, 'epi/globals/cadastrar_usuario.html', {'usuario':usuario})
    return render(request, 'epi/globals/cadastrar_usuario.html')
from django.shortcuts import get_object_or_404, render, redirect
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
    # Tenta obter o equipamento, retorna 404 se não encontrado
    equipamento = get_object_or_404(Equipamento, id=id)
    if request.method == 'POST':
        nome = request.POST.get('nome')
        ca = request.POST.get('ca')
        validade = request.POST.get('validade')
        
        # Validação mais robusta
        if not (nome and ca and validade):
            return render(request, 'epi/globals/atualizar.html', {
                'equipamento': equipamento,
                'error': 'Todos os campos devem ser preenchidos'
            })

        try:
            # Tente converter a validade para o tipo de dado correto (por exemplo, data)
            equipamento.nome = nome
            equipamento.ca = ca
            equipamento.validade = validade
            equipamento.save()
            return redirect(f'/listar_epi/{equipamento.id}')  # Redireciona para a página de detalhes
        except ValueError:
            return render(request, 'epi/globals/atualizar.html', {
                'equipamento': equipamento,
                'error': 'Dados inválidos, por favor verifique os campos.'
            })
    
    # Renderiza a página de atualização se o método for GET
    return render(request, 'epi/globals/atualizar.html', {'equipamento': equipamento})

#Listar EPIs
from django.shortcuts import render
from .models import Equipamento

def listar_epi(request):
    # Obtendo todos os equipamentos inicialmente
    values = Equipamento.objects.all()

    # Obtendo parâmetros de filtro da URL
    nome = request.GET.get('nome')
    ca = request.GET.get('ca')
    validade = request.GET.get('validade')

    # Aplicando filtros se os parâmetros forem fornecidos
    if nome:
        values = values.filter(nome__icontains=nome)
    if ca:
        values = values.filter(ca__icontains=ca)
    if validade:
        values = values.filter(validade__icontains=validade)

    # Retornando o contexto para o template
    return render(request, 'epi/globals/listar.html', {'equipamentos': values})
#Excluir
from django.shortcuts import render, get_object_or_404, redirect
from .models import Equipamento

def excluir_epi(request, id):
    equipamento = get_object_or_404(Equipamento, id=id)

    if request.method == 'POST':
        equipamento.delete()
        return redirect('listar_epi')  # Redireciona para a lista de EPIs após a exclusão

    return render(request, 'epi/globals/excluir.html', {'equipamento': equipamento})

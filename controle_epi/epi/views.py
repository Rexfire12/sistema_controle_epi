from django.shortcuts import render, redirect, get_object_or_404
from epi.models import Equipamento, Colaborador, Registro


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
        return redirect(listar_epi)
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
        return redirect(listar_colaborador)
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
            return redirect(listar_colaborador)
        else:
            return render(request, 'epi/globals/atualizar_colaborador.html', {'colaborador': colaborador, 'erro': True})
    return render(request, 'epi/globals/atualizar_colaborador.html', {'colaborador': colaborador})

#Excluir Colaboradores
def excluir_colaborador(request, id):    
    colaborador = Colaborador.objects.get(id=id)
    colaborador.delete()
    return redirect(atualizar_colaborador)      

#Regitrar Ação
def registrar_acao(request):
    if request.method == 'POST':
        equipamento = request.POST.get('equipamento')
        colaborador= request.POST.get('colaborador')
        data_emprestimo = request.POST.get('data_emprestimo')
        previsaodevolucao = request.POST.get('previsao_devolucao')
        status = request.POST.get('status')
        condicoes = request.POST.get('condicoes')
        data_devolucao = request.POST.get('data_devolucao')
        observacao = request.POST.get('observacao')

        # Verificar se equipamento e colaborador existem
        equipamento = get_object_or_404(Equipamento, nome=equipamento)
        colaborador = get_object_or_404(Colaborador, nome=colaborador)

        # Criar o registro
        acao = Registro.objects.create(
            equipamento=equipamento,
            colaborador=colaborador,
            data_emprestimo=data_emprestimo,
            previsao_devolucao=previsaodevolucao,
            status=status,
            condicoes=condicoes,
            data_devolucao=data_devolucao,
            observacao=observacao
        )
        return redirect(listar_acao)

    return render(request, 'epi/globals/registrar_acao.html', {'acao': None})

#Listar Ações
def listar_acao(request):
    values = Registro.objects.all()
    pesquisa = request.GET.get('nome_colaborador')
    if pesquisa:
        values = values.filter(colaborador__nome__icontains=pesquisa)
    colaborador = request.GET.get('colaborador')
    equipamento = request.GET.get('equipamento')
    data_emprestimo = request.GET.get('data_emprestimo')
    previsaodevolucao = request.GET.get('previsaodevolucao')
    status = request.GET.get('status')
    condicoes = request.GET.get('condicoes')
    data_devolucao = request.GET.get('data_devolucao')
    observacao = request.GET.get('observacao')
    

    if colaborador:
        values = values.filter(colaborador__nome__icontains=colaborador)
    if equipamento:
        values = values.filter(equipamento__nome__icontains=equipamento)
    if data_emprestimo:
        values = values.filter(data_emprestimo__icontains=data_emprestimo)
    if previsaodevolucao:
        values = values.filter(previsao_devolucao__icontains=previsaodevolucao)
    if status:
        values = values.filter(status__icontains=status)
    if condicoes:
        values = values.filter(condicoes__icontains=condicoes)
    if data_devolucao:
        values = values.filter(data_devolucao__icontains=data_devolucao)
    if observacao:
        values = values.filter(observacao__icontains=observacao)
    filtered_values = values.values('equipamento__nome', 'colaborador__nome', 'data_emprestimo', 'previsao_devolucao', 'status', 'condicoes', 'data_devolucao', 'observacao')if values.exists() else []
    return render(request, 'epi/globals/listar_acao.html', {'acoes': filtered_values})
#Atualizar Ações
def atualizar_acao(request, id=0):
    if id == 0:
        if request.method == 'GET' and request.GET.get('nome_colaborador'):
            nome_colaborador = request.GET.get('nome_colaborador').strip()
            acoes = Registro.objects.filter(colaborador__nome__icontains=nome_colaborador)
        else:
            acoes = Registro.objects.all()
        return render(request, 'epi/globals/atualizar_acao.html', {'acoes': acoes})
    acao = get_object_or_404(Registro, id=id)
    if request.method == 'POST':
        equipamento = request.POST.get('equipamento')
        colaborador = request.POST.get('colaborador')
        data_emprestimo = request.POST.get('data_emprestimo')
        previsao_devolucao = request.POST.get('previsao_devolucao')
        status = request.POST.get('status')
        condicoes = request.POST.get('condicoes')
        data_devolucao = request.POST.get('data_devolucao')
        observacao = request.POST.get('observacao')
        if equipamento and colaborador and data_emprestimo and previsao_devolucao and status and condicoes and data_devolucao and observacao:
            equipamento = get_object_or_404(Equipamento, nome=equipamento)
            colaborador = get_object_or_404(Colaborador, nome=colaborador) 
            acao.equipamento = equipamento
            acao.colaborador = colaborador
            acao.data_emprestimo = data_emprestimo            
            acao.previsao_devolucao = previsao_devolucao
            acao.status = status
            acao.condicoes = condicoes
            acao.data_devolucao = data_devolucao
            acao.observacao = observacao
            acao.save()
            return redirect(listar_acao)
        else:
            return render(request, 'epi/globals/atualizar_acao.html', {'acao': acao, 'erro': True})
    return render(request, 'epi/globals/atualizar_acao.html', {'acao': acao})

#Excluir Ações
def excluir_acao(request, id=0):
    acao = Registro.objects.get(id=id)
    acao.delete()
    return redirect(listar_acao)
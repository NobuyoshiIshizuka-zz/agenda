from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect
from .models import Contato
from django.core.paginator import Paginator
from django.db.models import Q, Value  # Para fazer consultas mais complexas
from django.db.models.functions import Concat
from django.contrib import messages


def index(request):
    contatos = Contato.objects.order_by('-id').filter(
        mostrar=True
    )
    paginator = Paginator(contatos, 10)  # Exibindo 10 contatos por página

    page = request.GET.get('p')
    contatos = paginator.get_page(page
                                  )
    return render(request, 'contatos/index.html', {
        'contatos': contatos
    })


def ver_contato(request, contato_id):
    contato = get_object_or_404(Contato, id=contato_id)

    if not contato.mostrar:
        raise Http404()

    return render(request, 'contatos/ver_contato.html', {
        'contato': contato
    })

def busca(request):
    termo = request.GET.get('termo')

    if termo is None or not termo:  # Se o termo estiver nulo ou vázio levante o erro 404
        messages.add_message(request, messages.ERROR, 'Campo termo não pode ficar vazio.')
        return redirect('index')

    campos = Concat('nome', Value(' '), 'sobrenome')

    contatos = Contato.objects.annotate(
        nome_completo = campos).filter(
        Q(nome_completo__icontains=termo) | Q(telefone__icontains=termo)  # Buscando pelo nome ou telefone
    )
    paginator = Paginator(contatos, 10)  # Exibindo 10 contatos por página

    page = request.GET.get('p')
    contatos = paginator.get_page(page
                                  )
    return render(request, 'contatos/busca.html', {
        'contatos': contatos
    })


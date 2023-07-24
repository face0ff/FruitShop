from django.shortcuts import render

from transaction.models import Transaction


def index(request):
    transactions = Transaction.objects.order_by('-id')[:40]
    context = {
        'transactions': transactions
    }
    return render(request, 'index.html', context)


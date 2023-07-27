from django.shortcuts import render

from bank.models import Bank
from chat.models import Chat
from stock.models import Stock
from transaction.models import Transaction
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from chat.tasks import task_print_joke


def start_joke():
    # joke = Chat.objects.count()
    task_print_joke.apply_async(queue='joke')


# Create your views here.
def login_page(request):
    print('lol')


def logout_page(request):
    logout(request)
    return redirect('index')

def index(request):

    if request.method == 'POST':
        print(request.POST)
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is None:
            messages.info(request, 'Неверный логин или пароль')
        else:
            login(request, user)
            return redirect('index')
    chat = Chat.objects.order_by('date')[:40]
    transactions = Transaction.objects.order_by('-id')[:40]
    items = Stock.objects.all()
    bank_score = Bank.objects.first()
    context = {
        'chat': chat,
        'bank_score': bank_score,
        'items': items,
        'transactions': transactions
    }
    return render(request, 'index.html', context)


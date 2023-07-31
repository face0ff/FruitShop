import datetime

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

from bank.models import Bank, File
from bank.views import edit_bank
from chat.models import Chat
from stock.models import Stock
from transaction.models import Transaction
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from chat.tasks import task_print_joke
from transaction.tasks import buy, sell


def start_joke(request):
    print('111111111111111111111111111111111111111111111111')
    # joke = Chat.objects.count()
    task_print_joke.apply_async(queue='joke')
    return HttpResponse({True})

def buy_fruit(request):
    fruit_id = request.GET.get('id')
    count = request.GET.get('count')
    print(fruit_id, count)
    response = buy(int(fruit_id), int(count))
    return HttpResponse({response})

def sell_fruit(request):
    fruit_id = request.GET.get('id')
    count = request.GET.get('count')
    print(fruit_id, count)
    response = sell(int(fruit_id), int(count))
    return HttpResponse({response})

def add_bank(request):
    amount = request.GET.get('amount')
    edit_bank(int(amount), True)
    return HttpResponse(f"add_bank: {amount}")

def sub_bank(request):
    amount = request.GET.get('amount')
    edit_bank(int(amount), False)
    return HttpResponse(f"add_bank: {amount}")


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
    current_day = datetime.datetime.today().day
    if File.objects.filter(date__day=current_day).count():
        files = File.objects.filter(date__day=current_day).count()
    else:
        files = 0
    chat = Chat.objects.all().order_by('-id')[:40][::-1]
    transactions = Transaction.objects.order_by('-id')[:40]
    items = Stock.objects.all()
    bank_score = Bank.objects.first()
    context = {
        'files': files,
        'chat': chat,
        'bank_score': bank_score,
        'items': items,
        'transactions': transactions
    }
    return render(request, 'index.html', context)

def upload_file(request):
    print('343')
    if request.method == 'POST' and request.FILES.get('file'):
        print('123123')
        uploaded_file = request.FILES['file']
        # Save the file to the database
        uploaded_file_obj = File.objects.create(file=uploaded_file)
        uploaded_file_obj.save()

        return JsonResponse({'message': 'File uploaded and saved successfully.'})

    return JsonResponse({'message': 'File upload failed.'}, status=400)
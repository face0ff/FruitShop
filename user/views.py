from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect


# Create your views here.
# def login_page(request):
#
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password1')
#         user = authenticate(request, username=username, password=password)
#         if user is None:
#             messages.info(request, 'Неверный логин или пароль')
#         else:
#             login(request, user)
#             request.LANGUAGE_CODE = user.language
#             return redirect('')
#
#     context = {}
#     return render(request, '', context)
#
# def logout_page(request):
#     logout(request)
#     return redirect('')
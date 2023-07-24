from django.shortcuts import render

# Create your views here.
def edit_stock(price, status):
    bank_score = Bank.objects.first()
    if status:
        bank_score.score = bank_score.score - price
    else:
        bank_score.score = bank_score.score + price
    bank_score.save()
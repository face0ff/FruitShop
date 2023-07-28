from django.urls import path, include
from FruitShop import views

urlpatterns = [
    path('', views.index, name='index'),
    path('logout/', views.logout_page, name='logout_page'),
    path('', views.start_joke, name='start_joke'),
    path('buy_fruit/', views.buy_fruit, name='buy_fruit'),
    path('sell_fruit/', views.sell_fruit, name='sell_fruit'),
    path('add_bank/', views.add_bank, name='add_bank'),
    path('sub_bank/', views.sub_bank, name='sub_bank'),
    path('upload_file/', views.upload_file, name='upload_file'),

]

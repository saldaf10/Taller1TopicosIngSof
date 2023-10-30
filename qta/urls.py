from django.urls import path
from .views import home,mainscreen,more_info,exit,ticket, about, stadistics

urlpatterns = [
    path('', home, name='home'),
    path('mainscreen/', mainscreen, name='mainscreen'),
    path('about/', about, name='about'),
    path('mainscreen/more_info/<int:id_unico>/',more_info, name='more_info'),
    path('mainscreen/ticket/',ticket, name='ticket'),
    path('mainscreen/stadistics/',stadistics, name='stadistics'),
    path('logout/',exit, name='exit'),
    
]
from django.urls import path
from .views import home,mainscreen,more_info,exit,ticket, about, stadistics
from .views import TicketListView, TicketDetailView, TicketCreateView, TicketUpdateView, TicketDeleteView

urlpatterns = [
    path('', home, name='home'),
    path('mainscreen/', mainscreen, name='mainscreen'),
    path('about/', about, name='about'),
    path('mainscreen/more_info/<int:id_unico>/',more_info, name='more_info'),
    path('mainscreen/ticket/',ticket, name='ticket'),
    path('mainscreen/stadistics/',stadistics, name='stadistics'),
    path('logout/',exit, name='exit'),
    path('tickets/', TicketListView.as_view(), name='ticket_list'),
    path('tickets/<int:pk>/', TicketDetailView.as_view(), name='ticket_detail'),
    path('tickets/create/', TicketCreateView.as_view(), name='ticket_create'),
    path('tickets/<int:pk>/update/', TicketUpdateView.as_view(), name='ticket_update'),
    path('tickets/<int:pk>/delete/', TicketDeleteView.as_view(), name='ticket_delete'),
]
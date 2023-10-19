from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse
from .models import Ticket
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
import datetime


# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def exit(request):
    logout(request)
    return redirect('home')
 
@login_required
def mainscreen(request):
    
    searchState = request.GET.get('searchState')
    if searchState:
        tickets = Ticket.objects.filter(state__icontains=searchState)
    else:
          tickets = Ticket.objects.all()
    return render(request, 'mainscreen.html',{'searchState':searchState, 'tickets':tickets})

def more_info(request, id_unico):
    ticket = get_object_or_404(Ticket, id_unico=id_unico)
    

    if request.method == 'POST':
        ticket.call_time = request.POST.get('call_time')
        ticket.priority = request.POST.get('priority')
        ticket.discussion = request.POST.get('discussion')
        ticket.state = request.POST.get('state')
        ticket.place = request.POST.get('place')
        ticket.equipment = request.POST.get('equipment')
        ticket.contact_number = request.POST.get('contact_number')
        ticket.contact_name = request.POST.get('contact_name')
        ticket.first_follow_up = request.POST.get('first_follow_up')
        ticket.second_follow_up = request.POST.get('second_follow_up')
        ticket.third_follow_up = request.POST.get('third_follow_up')
        
        # Convertir la fecha a un objeto datetime
        call_time_datetime = datetime.datetime.strptime(ticket.call_time, '%d-%m-%Y %H:%M:%S')

        # Actualizar el campo call_time con el objeto datetime
        ticket.call_time = call_time_datetime
        
        ticket.save()
        
        return redirect('mainscreen')

    return render(request, 'more_info.html', {'ticket': ticket})

def ticket(request):
    if request.method == 'POST':
        ticket_number = request.POST.get('ticket_number')
        call_time = request.POST.get('call_time')
        priority = request.POST.get('priority')
        discussion = request.POST.get('discussion')
        state = request.POST.get('state')
        place = request.POST.get('place')
        equipment = request.POST.get('equipment')
        contact_number = request.POST.get('contact_number')
        contact_name = request.POST.get('contact_name')

        # Crea el nuevo ticket en la base de datos
        nuevo_ticket = Ticket(ticket_number=Ticket.objects.count()+1, call_time=call_time, priority=priority, discussion=discussion, state=state, place=place, equipment=equipment, contact_number=contact_number, contact_name=contact_name )
        nuevo_ticket.save()
        

        return redirect('mainscreen')

    return render(request, 'ticket.html')

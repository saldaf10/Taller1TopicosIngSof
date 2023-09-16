from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse
from .models import Ticket
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout


# Create your views here.
def home(request):
    return render(request, 'home.html')

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
        ticket.ticket_number = request.POST.get('ticket_number')
        ticket.call_time = request.POST.get('call_time')
        ticket.priority = request.POST.get('priority')
        ticket.discussion = request.POST.get('discussion')
        ticket.state = request.POST.get('state')
        ticket.source = request.POST.get('source')
        ticket.equipment = request.POST.get('equipment')
        ticket.contact_number = request.POST.get('contact_number')
        ticket.contact_name = request.POST.get('contact_name')
        
        ticket.save()

    return render(request, 'more_info.html', {'ticket': ticket})

def ticket(request):
    if request.method == 'POST':
        ticket_number = request.POST.get('ticket_number')
        call_time = request.POST.get('call_time')
        priority = request.POST.get('priority')
        discussion = request.POST.get('discussion')
        state = request.POST.get('state')
        source = request.POST.get('source')
        equipment = request.POST.get('equipment')
        contact_number = request.POST.get('contact_number')
        contact_name = request.POST.get('contact_name')

        # Crea el nuevo ticket en la base de datos
        nuevo_ticket = Ticket(ticket_number=ticket_number, call_time=call_time, priority=priority, discussion=discussion, state=state, source=source, equipment=equipment, contact_number=contact_number, contact_name=contact_name )
        nuevo_ticket.save()

        return mainscreen(request)

    return render(request, 'ticket.html')

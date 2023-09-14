from django.shortcuts import render
from django.http import HttpResponse
from .models import Ticket

# Create your views here.
def home(request):
    return render(request, 'home.html')
 
def mainscreen(request):
    tickets = Ticket.objects.all()
    return render(request, 'mainscreen.html',{'tickets':tickets})

def more_info(request):
    return render(request, 'more_info.html')

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

        return HttpResponse('Ticket creado exitosamente')  

    return render(request, 'ticket.html')

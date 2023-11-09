from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse
from .models import Ticket
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
import datetime
import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt
import csv

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
        ticket.Support_name = request.POST.get('Support_name')
        ticket.first_follow_up = request.POST.get('first_follow_up')
        ticket.second_follow_up = request.POST.get('second_follow_up')
        ticket.third_follow_up = request.POST.get('third_follow_up')
        
        if ticket.state == 'Completed':
            ticket.time_finish = datetime.datetime.now()
        
        # Convertir la fecha a un objeto datetime
        call_time_datetime = datetime.datetime.strptime(ticket.call_time, '%d-%m-%Y %H:%M:%S')

        # Actualizar el campo call_time con el objeto datetime
        ticket.call_time = call_time_datetime
        
        
        if request.POST.get('state') == 'Completed':
            ticket.call_time_finish = datetime.datetime.now()
            
        
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

@login_required
def stadistics(request):
    # Datos
    tickets = Ticket.objects.all()
    x = {}
    
    # Grafica #1: Equipo con más reportes #
    for element in tickets:
        if element.equipment in x.keys():
            x[element.equipment] += 1
        else:
            x[element.equipment] = 1
     
    Max = ("",-1)      
    for key in x.keys():
        if x[key] > Max[1]:
            Max = (key,x[key])

    # Crea la gráfica
    plt.figure()
    plt.bar(x.keys(), x.values())

    plt.savefig("graph.jpg")
    
    plt.clf()
    
    # Grafica #2: Histograma de Prioridades #
    priorities = [ticket.priority for ticket in tickets]

    df = pd.DataFrame({'priority': priorities})
    
    # Crea la gráfica #2: Histograma de Prioridades
    histogram_data = df['priority'].value_counts()
    histogram_data.plot(kind='bar', color='skyblue')
    plt.xlabel('Prioridad')
    plt.ylabel('Cantidad de Tickets')
    plt.xticks(rotation=0)
    plt.savefig("graph2.jpg")

    # Encuentra el valor más alto en el histograma
    max_priority_value = histogram_data.max()
    max_priority_name = histogram_data.idxmax()  # Nombre de la prioridad con el valor más alto
    
    # Limpio
    plt.clf()
    
    # Grafica #3: Tarta de estados
    df = pd.DataFrame(tickets.values('call_time', 'state'))
    fecha_actual = datetime.datetime.now()

    fecha_hace_una_semana = fecha_actual - datetime.timedelta(days=7)
    fecha_hace_una_semana = pd.to_datetime(fecha_hace_una_semana, utc=True)

    tickets_ultima_semana = df[df['call_time'] >= fecha_hace_una_semana]

    estado_counts = tickets_ultima_semana['state'].value_counts()
    
    if not estado_counts.empty:
        estado_mas_comun = estado_counts.idxmax()
    else:
        estado_mas_comun = "No Value"

    plt.pie(estado_counts, labels=estado_counts.index, autopct='%1.1f%%', startangle=140)

    plt.savefig("graph4.jpg")
    
    plt.clf()
    
    
    # Grafica 4
    df = pd.DataFrame(tickets.values('call_time', 'place'))
    fecha_actual = datetime.datetime.now()

    fecha_hace_una_semana = fecha_actual - datetime.timedelta(days=7)
    fecha_hace_una_semana = pd.to_datetime(fecha_hace_una_semana, utc=True)

    tickets_ultima_semana = df[df['call_time'] >= fecha_hace_una_semana]

    estado_counts = tickets_ultima_semana['place'].value_counts()
    
    plt.barh(estado_counts.index, estado_counts)
    plt.yticks(rotation=90)
    
    clinica_mas_comun = estado_counts.idxmax()

    plt.savefig("graph5.jpg")
    
    plt.clf()
    
    tickets = Ticket.objects.all()
    
    with open('statistics.csv', "w") as f:
        f.write(", ".join(['id', 'support', 'person', 'number person', 'place', 'equipment', 'state', 'priority', 'discussion', '1', '2', '3']) + "; \n")
        for ticket in tickets:
            f.write(", ".join([ticket.ticket_number, ticket.Support_name, ticket.contact_name, ticket.contact_number, ticket.place, ticket.place, ticket.equipment, ticket.state, ticket.priority, ticket.discussion, ticket.first_follow_up, ticket.second_follow_up, ticket.third_follow_up]) + "; \n")

    return render(request, 'stadistics.html', {'Max_Equipment': Max[0], 'Max_Priority' : max_priority_name, 'Max_State': estado_mas_comun, 'Max_Place': clinica_mas_comun})
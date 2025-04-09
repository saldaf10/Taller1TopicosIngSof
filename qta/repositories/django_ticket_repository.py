# repositories/django_ticket_repository.py
from qta.models import Ticket
from qta.interfaces.ticket_repository_interface import ITicketRepository

class DjangoTicketRepository(ITicketRepository):
    def create(self, data):
        ticket = Ticket(**data)
        ticket.save()
        return ticket

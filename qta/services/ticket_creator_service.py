# services/ticket_creator_service.py
from qta.interfaces.ticket_repository_interface import ITicketRepository

class TicketCreatorService:
    def __init__(self, repo: ITicketRepository):
        self.repo = repo

    def execute(self, data):
        return self.repo.create(data)

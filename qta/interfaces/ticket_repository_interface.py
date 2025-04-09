# interfaces/ticket_repository_interface.py
from abc import ABC, abstractmethod

class ITicketRepository(ABC):
    @abstractmethod
    def create(self, data: dict):
        pass

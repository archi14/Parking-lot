from parking_lot.models.vehicle import Vehicle
from parking_lot.models.ticket import Ticket

class Slot():

    def __init__(self, type, number, floor_number, lot_id, ticket=None, booked=False, vehicle=None):
        self.type = type
        self.id = number
        self.floor_id = floor_number
        self.ticket = ticket
        self.lot_id = lot_id
        self.booked = booked
        self.vehicle = vehicle

    def get_type(self):
        return self.type
    
    def get_id(self):
        return self.id
    
    def get_floor_id(self):
        return self.floor_id
    
    def book_slot(self, vehicle):
        self.ticket = Ticket(f'{self.lot_id}_{self.floor_id}_{self.id}')
        self.booked = True
        self.vehicle = vehicle

    def get_ticket(self):
        return self.ticket
    
    def unbook_slot(self):
        self.ticket = None
        self.booked = False
        self.vehicle = None

    def get_vehicle(self):
        return self.vehicle

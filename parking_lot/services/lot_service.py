from parking_lot.models.lot import Lot
from parking_lot.models.vehicle import Vehicle
from parking_lot.services.display_service import DisplayService
from parking_lot.services.parking_service import ParkingService

class LotService:
    parking_lot = {}
    display_service = {}
    parking_service={}
    current_id = None

    def add_lot(self, id, number_of_floors, number_of_slots):
        if id not in LotService.parking_lot.keys():
            LotService.parking_lot[id] = Lot(id, number_of_floors, number_of_slots)
            self.display_service[id] = DisplayService(LotService.parking_lot[id]) 
            self.parking_service[id] = ParkingService(LotService.parking_lot[id])
            print(f'Created parking lot {id} with {number_of_floors} floors and {number_of_slots} slots')
        
    def set_current_lot(self, current_id):
        LotService.current_id = current_id

    def get_lot(self, id):
        return self.parking_lot[id]

    def get_parking_lot(self, lot_id):
        if lot_id in LotService.parking_lot.keys():
            return LotService.parking_lot[lot_id]
    
    def display(self, display_type, slot_type):
        self.display_service[LotService.current_id].display(display_type,slot_type)

    def park_vehicle(self, vehicle_type, reg_no, color):
        vehicle = Vehicle(vehicle_type, reg_no, color)
        self.parking_service[LotService.current_id].park_vehicle(vehicle)
    
    def unpark_vehicle(self, ticket_number):
        self.parking_service[LotService.current_id].unpark_vehicle(ticket_number)






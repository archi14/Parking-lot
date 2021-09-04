class ParkingService:

    def __init__(self, parking_lot):
        self.parking_lot = parking_lot
    

    def park_vehicle(self, vehicle):
        for floor in self.parking_lot.floors.values():
            if floor.book_free_slot(vehicle):
                return 

        print('Parking lot is full')
    
    def unpark_vehicle(self, ticket_number):
        _, floor_id, slot_id = ticket_number.split('_')
        floor = self.parking_lot.floors[int(floor_id)]
        if not floor.unbook_slot(int(slot_id)):
            print(f'Ticket {ticket_number} is invalid')



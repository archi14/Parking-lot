from typing import TYPE_CHECKING
from parking_lot.models.floor import Floor
from parking_lot.models.bike_slot import BikeSlot
from parking_lot.models.truck_slot import TruckSlot
from parking_lot.models.car_slot import CarSlot

class Lot:
    
    def __init__(self, id, number_of_floors, number_of_slots):
        self.id = id
        self.floors = {}
        self.number_of_floors = number_of_floors
        self.number_of_slots = number_of_slots
        for floor_id in range(1, number_of_floors+1):
            self.floors[floor_id] = Floor(floor_id, number_of_slots, id)
            floor = self.floors[floor_id]
            for slot_id in range(1, number_of_slots):
                if slot_id==1:
                    floor.slots[slot_id] = TruckSlot(slot_id, floor_id,id)
                elif slot_id == 2 or slot_id == 3:
                    floor.slots[slot_id] = BikeSlot(slot_id, floor_id,id)
                else:
                    floor.slots[slot_id] = CarSlot(slot_id, floor_id, id)

    def get_id(self):
        return self.id

    def get_floors(self):
        return self.floors

    def get_number_of_floors(self):
        return self.number_of_floors
    
    def get_number_of_slots(self):
        return self.number_of_slots
        
    def get_floor(self, floor_id):
        if floor_id in self.floors:
            return self.floors[floor_id]

   
            

    
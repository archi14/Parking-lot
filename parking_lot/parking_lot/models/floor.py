from parking_lot.models.type import Type
class Floor:
    
    def __init__(self, id, number_of_slots, lot_id, slots={}):
        self.id = id
        self.lot_id = lot_id
        self.number_of_slots = number_of_slots
        self.slots=slots
        self.slot_count={}
        self.booked={}
        self.slot_count[Type.BIKE.name]=2
        self.slot_count[Type.CAR.name]=self.number_of_slots-3
        self.slot_count[Type.TRUCK.name]=1
        self.booked[Type.BIKE.name]=[]
        self.booked[Type.CAR.name]=[]
        self.booked[Type.TRUCK.name]=[]
    
    def get_id(self):
        return self.id
    
    def get_slots(self):
        return self.slots
    
    def get_slot(self, slot_id):
        if slot_id not in self.slots.keys():
            return 0
        return self.slots[slot_id]
    
    def book_free_slot(self, vehicle):
        slot_type = vehicle.get_type()
        if len(self.booked[slot_type]) == self.slot_count[slot_type]:
            return 0
        if len(self.booked[slot_type]) == 0:
            to_be_booked = Type[slot_type].value
        else:
            to_be_booked = self.booked[slot_type][-1] + 1

        self.booked[slot_type].append(to_be_booked)
        slot = self.get_slot(to_be_booked)
        slot.book_slot(vehicle)
        print(f'Vehicle Parked. Ticket is {slot.ticket.id}')
        return 1

    def unbook_slot(self, slot_id):
        slot = self.get_slot(slot_id)
        if slot == 0:
            return slot
        slot_type = slot.get_type()
        vehicle = slot.get_vehicle()
        if slot_id not in self.booked[slot_type]:
            return 0
        self.booked[slot_type].remove(slot_id)
        slot.unbook_slot()
        print(f'Unparked vehicle with Registration Number: {vehicle.get_registration_number()} and color: {vehicle.color}')


    def get_free_slots_count(self, slot_type):
        if len(self.booked[slot_type])==0:
            return self.slot_count[slot_type]
        return self.slot_count[slot_type] - len(self.booked[slot_type])
    
    def get_alloted_slots(self, slot_type):
        return self.booked[slot_type]
    
    def get_free_slots(self, slot_type):

        return [slot for slot in range(Type[slot_type].value,Type[slot_type].value+self.slot_count[slot_type]) if slot not in self.booked[slot_type]]

        

    
    
    
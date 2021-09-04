class DisplayService:

    def __init__(self, parking_lot):
        self.parking_lot = parking_lot
    
    def display(self, display_type, vehicle_type):
        if display_type == 'free_count':
            return self.display_free_count(vehicle_type)
        if display_type == 'free_slots':
            return self.display_free_slots(vehicle_type)
        if display_type == 'occupied_slots':
            return self.display_occupied_slots(vehicle_type)
        
    def display_free_slots(self, vehicle_type):
        for floor in self.parking_lot.floors.values():
            free_slots = floor.get_free_slots(vehicle_type)
            print(f'Free slots for {vehicle_type} on floor {floor.get_id()}: {free_slots}')

    def display_free_count(self, vehicle_type):
        for floor in self.parking_lot.floors.values():
            count = floor.get_free_slots_count(vehicle_type)
            print(f'No. of free slots for {vehicle_type} on floor {floor.get_id()}: {count}')

    def display_occupied_slots(self, vehicle_type):
        for floor in self.parking_lot.floors.values():
            alloted_slots = floor.get_alloted_slots(vehicle_type)
            print(f'slots allocated for {vehicle_type} on floor {floor.get_id()}: {alloted_slots} ')

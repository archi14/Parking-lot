from parking_lot.services.lot_service import LotService
def get_input():
    lot_service = LotService()

    while True:
        command = input()
        commands = command.split(" ")
        
        if commands[0] == 'create_parking_lot':
            id, number_of_floors, number_of_slots = commands[1],int(commands[2]),int(commands[3])
            lot_service.add_lot(id, number_of_floors, number_of_slots)
            lot_service.set_current_lot(id)
        
        elif commands[0] == 'display':
            display_type, vehicle_type = commands[1], commands[2]
            lot_service.display(display_type, vehicle_type)
        
        elif commands[0] == 'park_vehicle':
            vehicle_type, reg_no, color = commands[1],commands[2],commands[3]
            lot_service.park_vehicle(vehicle_type,reg_no, color)
        
        elif commands[0] == 'unpark_vehicle':
            ticket_number = commands[1]
            lot_service.unpark_vehicle(ticket_number)

        else:
            break


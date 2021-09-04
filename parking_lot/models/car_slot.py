from parking_lot.models.slot import Slot
from parking_lot.models.type import Type
class CarSlot(Slot):
    def __init__(self, id, floor_id,lot_id, booked=False):
        super().__init__(Type.CAR.name, id, floor_id,lot_id)
        self.booked = booked
    
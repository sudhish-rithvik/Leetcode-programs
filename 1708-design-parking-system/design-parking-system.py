class ParkingSystem(object):

    def __init__(self, big, medium, small):
        self.slots = [0, big, medium, small]

    def addCar(self, carType):
        if self.slots[carType] > 0:
            self.slots[carType] -= 1
            return True
        return False
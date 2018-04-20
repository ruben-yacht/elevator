from Elevator import Elevator

class Customer:
    ''' explain class functionality'''

    def __init__(self, start_floor, destination_floor):
        self.start_floor = start_floor
        self.destination_floor = destination_floor
        self.in_elevator = False
        self.arrived = False

    def __str__(self):
        return "Customer (who goes from floor " + str(self.start_floor) + " to " + str(self.destination_floor) + ")"

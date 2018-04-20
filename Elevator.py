#from Customer import Customer
#from ElevatorStrategy import ElevatorStrategy
from DefaultStrategy import DefaultStrategy

class Elevator:
    ''' explain class functionality'''

    def __init__(self, total_floors=1, strategy=None):
        self.customers = set()
        self.total_floors = total_floors
        self.current_floor = 0
        self.strategy = strategy()
        self.stomach = set()

    def add_customer(self,c):
        self.customers.add(c)

    def remove_customer(self,c):
        self.customers.remove(c)

    def eat_customer(self,c):
        self.stomach.add(c)

    def throw_out_customer(self,c):
        self.stomach.remove(c)

    def start(self):
        print('The elevator starts.')
        self.strategy.calculate_floor_order(self.customers, self.total_floors)

        while not self.strategy.is_finished():
            self.go_to_floor(self.strategy.next_floor())
            for c in self.customers:
                if c.start_floor == self.current_floor:
                    if not c.in_elevator and not c.arrived:
                        self.eat_customer(c)
                        c.in_elevator = True
                        print("I ate a", c)
                elif c.destination_floor == self.current_floor:
                    if c.in_elevator:
                        self.throw_out_customer(c)
                        c.in_elevator = False
                        c.arrived = True
                        print("I spit out a", c)

    def go_to_floor(self, floor):
        self.current_floor = floor
        print('Elevator arrives at floor', floor)


    def stop(self):
        print('The elevator stops.')

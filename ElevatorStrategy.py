from abc import ABC, abstractmethod

class ElevatorStrategy(ABC):
    ''' explain class functionality'''

    @abstractmethod
    def __init__(self):
        self.current_index = 0
        self.floor_order = []

    @abstractmethod
    def next_floor(self):
        pass
    @abstractmethod
    def calculate_floor_order(self, customers, total_floors):
        self.customers = customers
        self.total_floors = total_floors
        print('The Strategy is calculating the floor order for', len(customers), "customers and",total_floors,"floors")

    @abstractmethod
    def is_finished(self):
        pass

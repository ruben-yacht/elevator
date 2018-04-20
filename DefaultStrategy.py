from ElevatorStrategy import ElevatorStrategy

class DefaultStrategy(ElevatorStrategy):
    ''' Strategy where the elevator goes from the ground floor to the top and back, stopping at every single floor.'''

    def __init__(self):
        super().__init__()
        print('initializing strategy')

    def next_floor(self):
        super().next_floor()
        #print('The Strategy instructs the next floor.')
        try:
            next = self.floor_order[self.current_index]
        except IndexError:
            next = None

        self.current_index += 1
        return next


    def calculate_floor_order(self, customers, total_floors):
        super().calculate_floor_order(customers, total_floors)
        order = []
        for i in range(0,self.total_floors - 1):
            order.append(i)
        for i in range(self.total_floors - 1, -1, -1):
            order.append(i)
        print("Floor order: ", order)

        self.floor_order = order

    def is_finished(self):
        super().is_finished()
        if self.current_index == len(self.floor_order):
            return True
        else:
            return False

from Elevator import Elevator
from Customer import Customer
from DefaultStrategy import DefaultStrategy
import random


class ElevatorGuy:
    '''
    The ElevatorGuy creates and starts the elevatorself.
    Customers tell the ElevatorGuy which floor they go to.
    '''

    def __init__(self):
        self.num_customers = self.get_user_int("How many customers? ",1,24)
        self.num_floors = self.get_user_int("How many floors? ", 1, 100)
        self.customers = self.gather_customers()

        print("Gathered ", self.num_customers, "customers for", self.num_floors,"floors.")
        self.elevator = Elevator(self.num_floors, DefaultStrategy)
        for c in self.customers:
            self.elevator.add_customer(c)


        print("Customers in elevator:")
        for c in self.elevator.customers:
            print(str(c))



        self.elevator.start()

    def get_user_int(self, message, minimum, maximum):
        mn = minimum
        mx = maximum
        msg = message
        while True:
            try:
                user_int = int(input(msg))
                if(user_int < mn or user_int > mx ):
                    print("Please provide a number between",mn,"and",mx)
                    continue
            except ValueError:
                print("Please provide a number between",mn,"and",mx)
                continue
            else:
                break
        return user_int

    def gather_customers(self):
        customers = []

        for i in range(0, self.num_customers):
            start = random.randint(1, self.num_floors)
            end = start
            while end == start:
                end = random.randint(1, self.num_floors)
            c = Customer(start,end)
            customers.append(c)

        return customers


if __name__ == "__main__":
    ElevatorGuy()

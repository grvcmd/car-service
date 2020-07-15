import time
from util import menu_functions


# Print out services
def print_services():
    print("Welcome to Davy's Auto Shop!")
    time.sleep(1)
    print("Here are the services we provide.")
    print('(1) Oil change -- $35')
    print('(2) Tire rotation -- $19')
    print('(3) Car wash -- $7')
    print('(4) Car wax -- $12')


services = {'Oil change': 35, 'Tire rotation': 19, 'Car wash': 7, 'Car wax': 12, '-': 0}


class Customer:
    def __init__(self, service1, service2):
        self.service1 = service1
        self.service2 = service2
        self.total = (services[self.service1] + services[self.service2])

    def print_invoice(self):
        if self.service1 in services and self.service1 != '-':
            print("\nService 1: {}, ${}".format(self.service1, str(services[self.service1])))
        elif self.service1 == '-':
            print("\nService 1: No service.")

        if self.service2 in services and self.service2 != '-':
            print("Service 2: {}, ${}".format(self.service2, str(services[self.service2])))
        elif self.service2 == '-':
            print("Service 2: No service.")

    def print_total(self):
        print("\nTotal: ${}".format(str(self.total)))


if __name__ == '__main__':
    print_services()

    customer = Customer(
        menu_functions.get_service1(),
        menu_functions.get_service2()
    )

    customer.print_invoice()
    customer.print_total()
import order

#   Logic model not hooked to DB

class DeliverySlot(object):
    def __init__(self, hour, car):
        self.hour = hour
        self.car = car
        self.active = True
        self.listOfOrders = []  #   list of Order.id

    def printSlot(self):
        output = "Slot (Hour: " + str(self.hour) + ") (Car: " + str(self.car) + ")"
        return output

    def changeActive(self, b):
        self.active = b

    def addOrder(self, Order, i, j):
        self.listOfOrders.append(Order)


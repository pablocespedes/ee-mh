import order
import json

"""
    This is a logic model
    Does not need to be hooked to the DB
"""
class DeliverySlot(object):
    def __init__(self, hour, car):
        self.hour = hour
        self.car = car
        self.active = None 
        self.listOfOrders = []  #   list of Order.id

    def printSlot(self):
        listOfAddresses = []
        for i, j in enumerate(self.listOfOrders):
            listOfAddresses.append(j.address)
        addressString = json.dumps(listOfAddresses)
        output = json.dumps(
                {
                    "Hour": str(self.hour), 
                    "Car": str(self.car), 
                    "Active": str(self.active), 
                    "NumOrders": str(len(self.listOfOrders)),
                    "Orders": addressString 
                }, 
                sort_keys=True, indent=4, separators=(',', ':'))
        return output

    def changeActive(self, b):
        self.active = b

    def addOrder(self, Order):
        self.listOfOrders.append(Order)

    def getLastOrder(self):
        return self.listOfOrders[-1]

    def getFirstOrder(self):
        return self.listOfOrders[0]


import random
import json

#   Reference to app/models/order.py

class Order(object):
    def __init__(self, address):
        self.address = address
        self.dummyDistance = random.uniform(0, 5)

    def getDistance(self, Order):
        """
            Implement Google Maps API here
        """
        return self.dummyDistance


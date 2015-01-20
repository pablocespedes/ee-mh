import random
import json

"""
    This is dummy object model simulating app/models/order.py
    Order objects are held in a list in DeliverySlot
"""

class Order(object):
    def __init__(self, address):
        self.address = address
        self.dummyDistance = random.uniform(0, 10)

    def getDistance(self, Order):
        """
            Implement Google Maps API here
        """
        return self.dummyDistance


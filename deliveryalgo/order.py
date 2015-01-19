import random

#   Reference to app/models/order.py

class Order(object):
    def __init__(self, address):
        self.address = address

    def getDistance(self, Order):
        return random.uniform(0, 10)

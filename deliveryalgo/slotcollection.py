import deliveryslot
from pprint import pprint

"""
    This is a container for DeliverySlot logic model instances
    The container is a simple 2D list
    Does not need to be hooked to the DB
"""

class SlotCollection(object):
    def __init__(self, h, c):
        self.numHours = h
        self.numCars = c
        self.slot2DList = self.buildSlotCollection() 
    
    def buildSlotCollection(self):
        hourList = []   #   begin with 0
        for h in range(self.numHours):
            tempCarList = []
            for c in range(self.numCars):
                tempSlot = deliveryslot.DeliverySlot(h+1,c+1)
                tempCarList.append(tempSlot)
            hourList.append(tempCarList)
        return hourList

    def addOrderToSlot(self, hour, car, order):
        h = hour - 1
        c = car - 1
        self.slot2DList[h][c].addOrder(order)

    def getSlot(self, hour, car):
        h = hour - 1
        c = car - 1
        return self.slot2DList[h][c]

    def outputCollectionActive(self):
        activeList = []   #   begin with 0
        for h in range(self.numHours):
            tempCarList = []
            tempCarList.append(h+1)
            for c in range(self.numCars):
                tempCarList.append(self.slot2DList[h][c].active)
            activeList.append(tempCarList)
        return pprint(activeList)


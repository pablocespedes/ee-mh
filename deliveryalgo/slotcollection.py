import deliveryslot
from pprint import pprint

#   container object for deliveryslot

class SlotCollection(object):
    def __init__(self, h, c):
        self.numHours = h
        self.numCars = c
        self.slot2DList = self.buildSlotCollection() 
    
    def buildSlotCollection(self):
        tempSlot2DList = []
        carList = []    #   begin with 0
        hourList = []   #   begin with 0
        tempSlot2DList.append(hourList)
        tempSlot2DList.append(carList)

        #   build the DeliverySlots
        h = 0
        while h < self.numHours:
            c = 0
            while c < self.numCars:
                tempSlot = deliveryslot.DeliverySlot(h,c)
                tempSlot2DList[c].append(tempSlot)
                c = c + 1
            h = h + 1
        return tempSlot2DList

    def addOrderToSlot(self, hour, car, order):
        h = hour - 1
        c = car - 1
        self.slot2DList[c][h].addOrder(order)

    def getSlot(self, hour, car):
        h = hour - 1
        c = car - 1
        return self.slot2DList[c][h]

    def outputCollectionActive(self):
        tempList = []
        h = 0
        while h < self.numHours:
            c = 0
            tempSubList = []
            tempSubList.append(self.slot2DList[c][h].active)
            tempList.append(tempSubList)
            while c < self.numCars:
                c = c + 1
            h = h + 1
        return pprint(tempList)


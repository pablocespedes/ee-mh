import deliveryslot

#   container object for deliveryslot

class SlotCollection(object):
    
    def buildSlotCollection(self):
        beginHour = 1
        numHours = 8
        numCars = 2
        slot2DList = []
        carList = []    #   begin with 0
        hourList = []   #   begin with 0
        slot2DList.append(carList)
        slot2DList.append(hourList)

        #   build the Slots
        #   all are Active
        h = beginHour 
        while h <= numHours:
            c = 0
            while c < numCars:
                tempSlot = deliveryslot.DeliverySlot(h,c)
                slot2DList[c].append(tempSlot)
                print tempSlot.printSlot()
                c = c + 1
            h = h + 1
        return slot2DList



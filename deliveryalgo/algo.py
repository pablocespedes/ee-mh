import order
import deliveryslot
import slotcollection

def dynamicDeliveryEngine():
    """
        (C)
            if above(2) _AND_ below(3) do not exist DeliverySlot.active = True 
    """
    h = 0
    while h < sc.numHours:
        c = 0
        while c < sc.numCars:
            """
                (C)
            """
            #   if in 1st h slots _AND_ slot below is empty
            if h == 0 and len(sc.slot2DList[c][h+1].listOfOrders) == 0:  
                sc.slot2DList[c][h].active = True
            
            #   if in last h slots _AND_ slot above is empty
            elif h == sc.numHours-1 and len(sc.slot2DList[c][h-1].listOfOrders) == 0:
                sc.slot2DList[c][h].active = True

            #   if slot above is empty _AND_ slot below is empty
            elif len(sc.slot2DList[c][h-1].listOfOrders) == 0 and len(sc.slot2DList[c][h+1].listOfOrders) == 0:
                sc.slot2DList[c][h].active = True

            c = c + 1
        h = h + 1
   
if __name__ == "__main__":
    #   new SlotCollection object filled with DeliverySlots
    sc = slotcollection.SlotCollection(12, 2)
   
    """
        Simulations & checks
    """
    #   simulate a few arbitrary Orders
    ao1 = order.Order("123 Park Ave")
    ao2 = order.Order("15 Park Ave")
    ao3 = order.Order("20 Park Ave")
    ao4 = order.Order("456 Park Ave")
    ao5 = order.Order("456 5th Ave")

    #   add Orders to a DeliverySlot(hour, car)
    sc.addOrderToSlot(12, 1, ao1)
    sc.addOrderToSlot(12, 2, ao2)
    sc.addOrderToSlot(9, 1, ao3)
    sc.addOrderToSlot(8, 2, ao4)
    sc.addOrderToSlot(1, 2, ao5)
   
    #   pre-algo checks 
    #print(sc.getSlot(1,1).printSlot())
    #print(sc.getSlot(1,2).printSlot())

    #   see what the last order was for a slot
    #lo1 = sc.getSlot(1,1).getLastOrder()
    #print (lo1.address)
   
    """
        New User Order
    """
    #   simulate adding the User's Order
    newUserOrder = order.Order("315 East 21st")
    print (ao1.getDistance(newUserOrder))

    """
        Initiate slot logic
    """
    dynamicDeliveryEngine()
 
    """
        Check slot logic outputs
    """  
    print(sc.getSlot(10,1).printSlot())
    print(sc.getSlot(10,2).printSlot())

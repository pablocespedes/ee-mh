import order
import deliveryslot
import slotcollection

def dynamicClusteringEngine(_sc, po):
    """
        Notation:
            (1) current slot
            (2) car is coming from slot aka above slot
            (3) car is going-to slot aka below slot

        (z)         distance between current and last of adjacent slots 
        (y)         distance between current and last of current slot 
        
        (B)
            (B1)    distance between last of the above(2) and the current(1)
            (B2)    distance between last of the current(1) and the below(3)
                
        (C)
            (C1)    boolean last of the above(2) DNE or is empty
            (C2)    boolean last of the below(3) DNE or is empty
    """
    z = 5 
    y = 1
    h = 0
    circuitBreakerDistance = 10 #   if > this all slots inactive
    while h < _sc.numHours:
        c = 0
        while c < _sc.numCars:
            
            #   if in 1st h slots _AND_ slot below is empty
            if h == 0 and len(_sc.slot2DList[c][h+1].listOfOrders) == 0:  
                _sc.slot2DList[c][h].active = True
            
            #   if in last h slots _AND_ slot above is empty
            elif h == _sc.numHours-1 and len(_sc.slot2DList[c][h-1].listOfOrders) == 0:
                _sc.slot2DList[c][h].active = True

            #   if slot above is empty _AND_ slot below is empty
            elif len(_sc.slot2DList[c][h-1].listOfOrders) == 0 and len(_sc.slot2DList[c][h+1].listOfOrders) == 0:
                _sc.slot2DList[c][h].active = True
            
            #   if slot above is !empty _AND_ slot below is empty
                #   dis(above, current) <= z _AND_ dis(current, last) <= y 
            elif len(_sc.slot2DList[c][h-1].listOfOrders) > 0 and len(_sc.slot2DList[c][h+1].listOfOrders) == 0:
                if len(_sc.slot2DList[c][h].listOfOrders) > 0:
                    if po.getDistance(_sc.slot2DList[c][h-1].getLastOrder()) <= z and po.getDistance(_sc.slot2DList[c][h].getLastOrder()) <= y:
                        _sc.slot2DList[c][h].active = True
                if len(_sc.slot2DList[c][h].listOfOrders) == 0:
                    if po.getDistance(_sc.slot2DList[c][h-1].getLastOrder()) <= z:
                        _sc.slot2DList[c][h].active = True
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
    sc.addOrderToSlot(10, 1, order.Order("123 Main St"))
    sc.addOrderToSlot(10, 1, order.Order("123 Line St"))
   
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
    print (newUserOrder.getDistance(ao1))    #   dummy pass

    """
        Initiate slot logic
    """
    dynamicClusteringEngine(sc, newUserOrder)
 
    """
        Check slot logic outputs
    """  
    print(sc.getSlot(10,1).printSlot())
    #print(sc.getSlot(10,2).printSlot())
    print(sc.getSlot(5,2).printSlot())

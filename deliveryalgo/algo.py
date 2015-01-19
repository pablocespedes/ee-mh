import order
import deliveryslot
import slotcollection

def dynamicClusteringEngine(_sc, po):
    """
        Notation:
            (1) current slot
            (2) car is coming from last order in the above slot
            (3) car is going-to first order in the below slot

        (z)         distance between first/last order in adjacent slots 
        (y)         distance between last order in current slot 

        (A)
                    distance between last of the current(1) and current(1)
        (B)
            (B1)    distance between last of the above(2) and current(1)
            (B2)    distance between first of the below(3) and current(1)
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
                #   if current slot is !empty
                """
                    Refactor to an external method isEmptyHelper
                    return boolean
                """
                if len(_sc.slot2DList[c][h].listOfOrders) > 0:
                    #   if dis(current, last) <=y
                    if po.getDistance(_sc.slot2DList[c][h].getLastOrder()) <= y:
                        _sc.slot2DList[c][h].active = True
                #   if current slot is !empty
                if len(_sc.slot2DList[c][h].listOfOrders) == 0:
                    _sc.slot2DList[c][h].active = True

            #   if in last h slots _AND_ slot above is empty
            elif h == _sc.numHours-1 and len(_sc.slot2DList[c][h-1].listOfOrders) == 0:
                #   if current slot is !empty
                if len(_sc.slot2DList[c][h].listOfOrders) > 0:
                    #   if dis(current, last) <=y
                    if po.getDistance(_sc.slot2DList[c][h].getLastOrder()) <= y:
                        _sc.slot2DList[c][h].active = True
                #   if current slot is !empty
                if len(_sc.slot2DList[c][h].listOfOrders) == 0:
                    _sc.slot2DList[c][h].active = True

            #   if slot above is empty _AND_ slot below is empty
            elif len(_sc.slot2DList[c][h-1].listOfOrders) == 0 and len(_sc.slot2DList[c][h+1].listOfOrders) == 0:
                #   if current slot is empty
                if len(_sc.slot2DList[c][h].listOfOrders) == 0:
                    _sc.slot2DList[c][h].active = True
                #   if current slot is !empty
                if len(_sc.slot2DList[c][h].listOfOrders) > 0:
                    # if dis(current, last) <=y
                    if po.getDistance(_sc.slot2DList[c][h].getLastOrder()) <=y:
                        _sc.slot2DList[c][h].active = True

            #   if slot above is !empty _AND_ slot below is empty
            #   (maybe use this slot)
                #   dis(last_above, current) <= z _AND_ dis(current, last) <= y 
                #   (distance from last_above to current <= z)
            elif len(_sc.slot2DList[c][h-1].listOfOrders) > 0 and len(_sc.slot2DList[c][h+1].listOfOrders) == 0:
                if len(_sc.slot2DList[c][h].listOfOrders) > 0:
                    if po.getDistance(_sc.slot2DList[c][h-1].getLastOrder()) <= z and po.getDistance(_sc.slot2DList[c][h].getLastOrder()) <= y:
                        _sc.slot2DList[c][h].active = True
                if len(_sc.slot2DList[c][h].listOfOrders) == 0:
                    if po.getDistance(_sc.slot2DList[c][h-1].getLastOrder()) <= z:
                        _sc.slot2DList[c][h].active = True
 
            #   if slot above is empty _AND_ slot below is !empty
            #   (maybe use this slot)
                #   dis(first_below, current) <= z _AND_ dis(current, last) <= y 
                #   (distance from curent to first_below <= z)
            elif len(_sc.slot2DList[c][h-1].listOfOrders) == 0 and len(_sc.slot2DList[c][h+1].listOfOrders) > 0:
                if len(_sc.slot2DList[c][h].listOfOrders) > 0:
                    if po.getDistance(_sc.slot2DList[c][h+1].getFirstOrder()) <= z and po.getDistance(_sc.slot2DList[c][h].getLastOrder()) <= y:
                            _sc.slot2DList[c][h].active = True
                if len(_sc.slot2DList[c][h].listOfOrders) == 0:
                    if po.getDistance(_sc.slot2DList[c][h+1].getFirstOrder()) <= z:
                        _sc.slot2DList[c][h].active = True

            #   if slot above is !empty _AND_ slot below is !empty
            elif len(_sc.slot2DList[c][h-1].listOfOrders) > 0 and len(_sc.slot2DList[c][h+1].listOfOrders) > 0:
                #   dis(last_above, current) <= z _AND_ dis(first_below, current) <= z 
                if po.getDistance(_sc.slot2DList[c][h-1].getLastOrder()) <=z and po.getDistance(_sc.slot2DList[c][h+1].getFirstOrder()) <= z:
                    #   if current slot is !empty
                    if len(_sc.slot2DList[c][h].listOfOrders) > 0:
                        #   if dis(current, last) <=y
                        if po.getDistance(_sc.slot2DList[c][h].getLastOrder()) <= y:
                            _sc.slot2DList[c][h].active = True
                    #   if current slot is !empty
                    if len(_sc.slot2DList[c][h].listOfOrders) == 0:
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
    
    #   add Orders to a DeliverySlot(hour, car)
    sc.addOrderToSlot(12, 1, ao1)
    sc.addOrderToSlot(10, 1, order.Order("300 2nd Ave"))
    sc.addOrderToSlot(10, 2, order.Order("101 Lex"))
    sc.addOrderToSlot(8, 1, order.Order("123 Main St"))
    sc.addOrderToSlot(8, 2, order.Order("987 Line Blvd"))
    sc.addOrderToSlot(9, 1, order.Order("456 Park Ave"))
    sc.addOrderToSlot(9, 2, order.Order("2000 5th Ave"))
   
    #   pre-algo checks 
    print(sc.getSlot(10,1).printSlot())
    print(sc.getSlot(9,1).printSlot())
 
    """
        New User Order
    """
    #   simulate adding the User's Order
    newUserOrder = order.Order("315 East 21st")
    print (newUserOrder.getDistance(ao1))    #   dummy pass

    """
        Initiate algo 
    """
    dynamicClusteringEngine(sc, newUserOrder)
 
    """
        Check slot logic outputs
    """  
    print(sc.getSlot(9,1).printSlot())
    print(sc.getSlot(9,2).printSlot())
    #print(sc.getSlot(10,2).printSlot())
    print(sc.outputCollectionActive())

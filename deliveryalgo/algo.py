import order
import deliveryslot
import slotcollection

"""
    Algo global params
"""
z = 5 
y = 1
h = 0

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
    for h in range(_sc.numHours): #   iterate rows
        for c in range(_sc.numCars):    #   iterate cols
            
            #   if in 1st h slots _AND_ slot below is empty
            if h == 0 and len(_sc.slot2DList[h+1][c].listOfOrders) == 0:  
                _sc.slot2DList[h][c].active = checkEmptyAndX(_sc, po, h, c)
            
            #   if in last h slots _AND_ slot above is empty
            elif h == _sc.numHours-1 and len(_sc.slot2DList[h-1][c].listOfOrders) == 0:
                _sc.slot2DList[h][c].active = checkEmptyAndX(_sc, po, h, c)
            
            #   if slot above is empty _AND_ slot below is empty
            elif len(_sc.slot2DList[h-1][c].listOfOrders) == 0 and len(_sc.slot2DList[h+1][c].listOfOrders) == 0:
                _sc.slot2DList[h][c].active = checkEmptyAndX(_sc, po, h, c)

            #   if slot above is !empty _AND_ slot below is empty
            #   (maybe use this slot)
            elif len(_sc.slot2DList[h-1][c].listOfOrders) > 0 and len(_sc.slot2DList[h+1][c].listOfOrders) == 0:
                #   dis(last_above, current) <= z _AND_ dis(current, last) <= y 
                #   (distance from last_above to current <= z)
                if len(_sc.slot2DList[h][c].listOfOrders) > 0:
                    if po.getDistance(_sc.slot2DList[h-1][c].getLastOrder()) <= z and po.getDistance(_sc.slot2DList[h][c].getLastOrder()) <= y:
                        _sc.slot2DList[h][c].active = True
                if len(_sc.slot2DList[h][c].listOfOrders) == 0:
                    if po.getDistance(_sc.slot2DList[h-1][c].getLastOrder()) <= z:
                        _sc.slot2DList[h][c].active = True
 
            #   if slot above is empty _AND_ slot below is !empty
            #   (maybe use this slot)
            elif len(_sc.slot2DList[h-1][c].listOfOrders) == 0 and len(_sc.slot2DList[h+1][c].listOfOrders) > 0:
                #   dis(first_below, current) <= z _AND_ dis(current, last) <= y 
                #   (distance from curent to first_below <= z)
                if len(_sc.slot2DList[h][c].listOfOrders) > 0:
                    if po.getDistance(_sc.slot2DList[h+1][c].getFirstOrder()) <= z and po.getDistance(_sc.slot2DList[h][c].getLastOrder()) <= y:
                            _sc.slot2DList[h][c].active = True
                if len(_sc.slot2DList[h][c].listOfOrders) == 0:
                    if po.getDistance(_sc.slot2DList[h+1][c].getFirstOrder()) <= z:
                        _sc.slot2DList[h][c].active = True

            #   if slot above is !empty _AND_ slot below is !empty
            elif len(_sc.slot2DList[h-1][c].listOfOrders) > 0 and len(_sc.slot2DList[h+1][c].listOfOrders) > 0:
                #   dis(last_above, current) <= z _AND_ dis(first_below, current) <= z 
                if po.getDistance(_sc.slot2DList[h-1][c].getLastOrder()) <=z and po.getDistance(_sc.slot2DList[h+1][c].getFirstOrder()) <= z:
                    _sc.slot2DList[h][c].active = checkEmptyAndX(_sc, po, h, c)

def checkEmptyAndX(_sc, po, h, c):
    #   if current slot is !empty
    if len(_sc.slot2DList[h][c].listOfOrders) > 0:
        #   if dis(current, last) <=y
        if po.getDistance(_sc.slot2DList[h][c].getLastOrder()) <= y:
            return True
    #   if current slot is !empty
    elif len(_sc.slot2DList[h][c].listOfOrders) == 0:
        return True
    return False

if __name__ == "__main__":
    #   new SlotCollection object filled with DeliverySlots
    sc = slotcollection.SlotCollection(12, 2) 
   
    """
        Simulations & checks
    """
    #   simulate a few arbitrary Orders
    ao1 = order.Order("123 Park Ave")
    ao2 = order.Order("237 14th St")
    
    #   add Orders to a DeliverySlot(hour, car)
    sc.addOrderToSlot(8, 1, ao1)
    sc.addOrderToSlot(8, 2, ao2)
    #sc.addOrderToSlot(9, 1, order.Order("456 Park Ave"))
    #sc.addOrderToSlot(9, 2, order.Order("2000 5th Ave"))
    sc.addOrderToSlot(10, 1, order.Order("300 2nd Ave"))
    sc.addOrderToSlot(10, 2, order.Order("101 Lex"))
    
    sc.addOrderToSlot(1, 1, order.Order("123 Main St"))
    sc.addOrderToSlot(1, 2, order.Order("987 Line Blvd"))
    
    #   pre-algo checks 
    print(sc.getSlot(9,1).printSlot())
    print(sc.getSlot(9,2).printSlot())
 
    """
        New User Order
    """
    #   simulate adding the User's Order
    newUserOrder = order.Order("315 East 21st")

    """
        Initiate algo 
    """
    dynamicClusteringEngine(sc, newUserOrder)
 
    """
        Check slot logic outputs
    """  
    print(sc.getSlot(9,1).printSlot())
    print(sc.getSlot(9,2).printSlot())
    
    """
        Check active on the full 2D list
    """
    sc.outputCollectionActive()
    print(newUserOrder.getDistance(ao1))    #   dummy pass

"""
    Algo global params
"""
z = 5 
y = 1
h = 0
circuitBreakerDistance = 10 #   if > this all slots inactive

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
    for h in range(_sc.numHours): #   iterate rows
        for c in range(_sc.numCars):    #   iterate cols
            
            #   if in 1st h slots _AND_ slot below is empty
            if h == 0 and len(_sc.slot2DList[h+1][c].listOfOrders) == 0:  
                _sc.slot2DList[h][c].active = checkCurrEmptyVersusY(_sc, po, h, c)
            
            #   if in 1st h slots _AND_ slot below is !empty
            if h == 0 and len(_sc.slot2DList[h+1][c].listOfOrders) > 0:  
                _sc.slot2DList[h][c].active = checkCurrEmptyVersusYAndVersusZToBelow(_sc, po, h, c)
            
            #   if in last h slots _AND_ slot above is empty
            elif h == _sc.numHours-1 and len(_sc.slot2DList[h-1][c].listOfOrders) == 0:
                _sc.slot2DList[h][c].active = checkCurrEmptyVersusY(_sc, po, h, c)
            #   if in last h slots _AND_ slot above is !empty
            elif h == _sc.numHours-1 and len(_sc.slot2DList[h-1][c].listOfOrders) > 0:
                _sc.slot2DList[h][c].active = checkCurrEmptyVersusYAndVersusZFromAbove(_sc, po, h, c)
            
            #   if slot above is empty and _AND_ slot below is empty
            elif len(_sc.slot2DList[h-1][c].listOfOrders) == 0 and len(_sc.slot2DList[h+1][c].listOfOrders) == 0:
                _sc.slot2DList[h][c].active = checkCurrEmptyVersusY(_sc, po, h, c)

            #   if slot above is !empty _AND_ slot below is empty
            #   (maybe use this slot)
            elif len(_sc.slot2DList[h-1][c].listOfOrders) > 0 and len(_sc.slot2DList[h+1][c].listOfOrders) == 0:
                _sc.slot2DList[h][c].active = checkCurrEmptyVersusYAndVersusZFromAbove(_sc, po, h, c)

            #   if slot above is empty _AND_ slot below is !empty
            #   (maybe use this slot)
            elif len(_sc.slot2DList[h-1][c].listOfOrders) == 0 and len(_sc.slot2DList[h+1][c].listOfOrders) > 0:
                _sc.slot2DList[h][c].active = checkCurrEmptyVersusYAndVersusZToBelow(_sc, po, h, c)

            #   if slot above is !empty _AND_ slot below is !empty
            elif len(_sc.slot2DList[h-1][c].listOfOrders) > 0 and len(_sc.slot2DList[h+1][c].listOfOrders) > 0:
                #   dis(last_above, current) <= z _AND_ dis(first_below, current) <= z 
                if po.getDistance(_sc.slot2DList[h-1][c].getLastOrder()) <=z and po.getDistance(_sc.slot2DList[h+1][c].getFirstOrder()) <= z:
                    _sc.slot2DList[h][c].active = checkCurrEmptyVersusY(_sc, po, h, c)
                elif po.getDistance(_sc.slot2DList[h-1][c].getLastOrder()) > z or po.getDistance(_sc.slot2DList[h+1][c].getFirstOrder()) > z:
                    _sc.slot2DList[h][c].active = False 

def checkCurrEmptyVersusY(_sc, po, h, c):
    #   if current slot is !empty
    if len(_sc.slot2DList[h][c].listOfOrders) > 0:
        #   if dis(current, last) <=y
        if po.getDistance(_sc.slot2DList[h][c].getLastOrder()) <= y:
            return True
    #   if current slot is empty
    elif len(_sc.slot2DList[h][c].listOfOrders) == 0:
        return True
    return False

def checkCurrEmptyVersusYAndVersusZFromAbove(_sc, po, h, c):
    #   dis(last_above, current) <= z _AND_ dis(current, last) <= y
    #   (distance from last_above to current <= z)
    if len(_sc.slot2DList[h][c].listOfOrders) > 0:
        if po.getDistance(_sc.slot2DList[h-1][c].getLastOrder()) <= z and po.getDistance(_sc.slot2DList[h][c].getLastOrder()) <= y:
            return True
    if len(_sc.slot2DList[h][c].listOfOrders) == 0:
        if po.getDistance(_sc.slot2DList[h-1][c].getLastOrder()) <= z:
            return True
    return False

def checkCurrEmptyVersusYAndVersusZToBelow(_sc, po, h, c):
    #   dis(first_below, current) <= z _AND_ dis(current, last) <= y 
    #   (distance from curent to first_below <= z)
    if len(_sc.slot2DList[h][c].listOfOrders) > 0:
        if po.getDistance(_sc.slot2DList[h+1][c].getFirstOrder()) <= z and po.getDistance(_sc.slot2DList[h][c].getLastOrder()) <= y:
            return True
    if len(_sc.slot2DList[h][c].listOfOrders) == 0:
        if po.getDistance(_sc.slot2DList[h+1][c].getFirstOrder()) <= z:
            return True
    return False

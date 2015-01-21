import order
import deliveryslot
import slotcollection
import algo

if __name__ == "__main__":
    #   new SlotCollection object filled with DeliverySlots
    sc = slotcollection.SlotCollection(10, 2) 
   
    """
        Simulations & checks
    """
    #   simulate a few arbitrary Orders
    ao1 = order.Order("123 Park Ave")
    ao2 = order.Order("237 14th St")
    
    #   add Orders to a DeliverySlot(hour, car)
#    sc.addOrderToSlot(1, 1, order.Order("100 3rd Ave"))
#    sc.addOrderToSlot(1, 2, order.Order("777 10th St"))
    sc.addOrderToSlot(2, 1, order.Order("372 9th St"))
    sc.addOrderToSlot(2, 2, order.Order("910 7th St"))
    sc.addOrderToSlot(8, 1, ao1)
    sc.addOrderToSlot(8, 2, ao2)
    sc.addOrderToSlot(9, 1, order.Order("456 Park Ave"))
    sc.addOrderToSlot(9, 2, order.Order("2000 5th Ave"))
    sc.addOrderToSlot(10, 1, order.Order("300 2nd Ave"))
    sc.addOrderToSlot(10, 2, order.Order("101 Lex"))
    sc.addOrderToSlot(6, 2, order.Order("101 Lex"))
    
#    sc.addOrderToSlot(1, 1, order.Order("123 Main St"))
#    sc.addOrderToSlot(1, 2, order.Order("987 Line Blvd"))
    
    #   pre-algo checks 
#    print(sc.getSlot(9,1).printSlot())
#    print(sc.getSlot(9,2).printSlot())
 
    """
        New User Order
    """
    #   simulate adding the User's Order
    newUserOrder = order.Order("315 East 21st")

    """
        Initiate algo 
    """
    algo.dynamicClusteringEngine(sc, newUserOrder)
 
    """
        Check slot logic outputs
    """  
#    print(sc.getSlot(9,1).printSlot())
#    print(sc.getSlot(9,2).printSlot())
    
    """
        Check active on the full 2D list
    """
    sc.outputCollectionActive()
    print(newUserOrder.getDistance(ao1))    #   dummy pass

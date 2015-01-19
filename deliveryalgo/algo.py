import order
import deliveryslot
import slotcollection

if __name__ == "__main__":
    slotcollection = slotcollection.SlotCollection()
    slotcollection.buildSlotCollection()

    #   simulate adding an arbitrary Order to slot(x, y)
    arbitraryOrder = order.Order("123 Park Ave") 

    #   simulate adding the User's Order
    newUserOrder = order.Order("456 5th Ave")
    print (arbitraryOrder.getDistance(newUserOrder))

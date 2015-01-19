# ee-mh

### /deliveryalgo
**algo.py**: main dynamic delivery engine algo.
**order.py**: order object, inherits from models/python.
**deliveryslot.py**: delivery slot object that holds a list of orders.
**slotcollection.py**: 2D container object of deliveryslots.

### in action
First instantiate a slotcollection, passing first the row slots (delivery hours), second the columns (delivery cars):

```python
newSlotCollection = slotcollection.SlotCollection(12,2)
```

Second add some orders to the ```newSlotCollection```.  Here we're adding a new order to the slot corresponding to the 8th hour and the 2nd car.  If delivery hours begin at, say, 11AM, then the 8th hour is actually 7PM.
```python
newSlotCollection.addOrderToSlot(8, 2, order.Order("123 Main Street")
```

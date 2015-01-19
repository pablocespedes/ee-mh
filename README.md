# ee-mh

## /deliveryalgo
**algo.py**: main dynamic delivery engine algo
**order.py**: order object, inherits from models/python
**deliveryslot.py**: delivery slot object that holds a list of orders
**slotcollection.py**: 2D container object of deliveryslots

### in action
First instantiate a slotcollection, passing first the row slots (delivery hours), second the columns (delivery cars):

```python
newSlotCollection = slotcollection.SlotCollection(12,2)
```

Second add some orders to the ```python newSlotCollection```. 

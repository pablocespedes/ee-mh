# ee-mh

## what it does
Tells the user whether a delivery slot is active or inactive.  Active or inactive states are based on the distances between all existing orders and the current order.  If a current order is within ```y``` distance of the **last** order in a slot then that slot is active.  If a current order is within ```z``` distance of the **last** order of an adjacent slot (+/- 1 hour) then that slot is active.  The presentation of active slots to a user given their current order is therefore path-dependent on all prior orders and non deterministic.

### the problem it solves
#### first the use case -- maximizing customer choice
Eateasy must deliver meals to not less than 5 unique customers every hour in Manhattan south of 59th Street.  Assume we have one delivery car.  The worst case for the delivery car is when John Doe in the Financial District and Jane Doe in Midtown West both select, say, the 1PM delivery hour.  This means that our car would have to drive from FiDi to Midtown.  If traffic was decent *maybe* our car could deliver both in an hour, but certainly it could not deliver more than these two.  To make matters works, Tom Doe of FiDi ordered for 2PM delivery, forcing the delivery car to make the trip back downtown.  Project this to infinity and you can see how unsustainable this can get.  A few solutions:
* Assign the delivery car to various zip codes for each hour.  This limits customer flexibility as they are blocked from certain delivery hours if their zip code does not correspond to that particular hour.  Customers will not be happy about this.
* Data mine order history and based on that history staff up an appropiate number of cars hour by hour.  This is great because it doesn't constrain customer choice.  But it requires a priori order history, which of course Eateasy doesn't have.
* Staff up a bunch of delivery cars and attempt to maximize utilization.  This is great for large organizations with substantial footprint and delivery infrastructure.  This is not a rational use of Eateasy resources however.

Bottom line: our use case is about maximizing the number of orders we can allocate per hour without limiting customer choice.

#### what we're not solving
Let's address what this does not solve.  It does not solve the class of [vehicle routing problems](http://en.wikipedia.org/wiki/Vehicle_routing_problem) or the class of [traveling salesman problems](http://en.wikipedia.org/wiki/Traveling_salesman_problem).  These problems are not relevant for Eateasy.  No matter how optimally we routed between FiDi and Midotwn, even with [UPS's 80 page algos](http://www.fastcompany.com/3004319/brown-down-ups-drivers-vs-ups-algorithm), we are physically incapable of delivering more than two orders in that hour without limiting customer choice.  Also optimal routing assumes a priori knowledge of your domain (e.g., the United States, downtown Miami, Zip Code 10010) and flexibility on when to make deliveries.  Eateasy will never have a priori knowledge of its domain nor do we have flexibility on when to make deliveries.  Our Manhattan-wide delivery schedule will change daily and our customers force us to delivery within certian hours.  UPS, the traveling salesmen, etc, have the luxury of knowledge of its domain and can pay visits whenever they please.  

#### the solution -- path dependent geographic clustering 
Because Eateasy cannot rely on a priori knowledge of its domain and has delivery time requirements we could overstaff and be "all places at once" waiting for deliveries.  This is obviously not a viable option.  Eateasy must therefore constrain customer choice so it doesn't have to be "all places at once" but must be careful not to alienate the customer.

Our solution is essentially first come first serve geographic clustering.  The first one into a slot "plants the flag" for that slot, and any future customer too far from that flag will not be able to select that slot.  The algo's parameters ensure we can deliver at least 5 orders per hour and ensure sufficient driving time to the next flag (cluster) to continue delivering 5 orders every hour.  Most important, we don't constrain our customer choices, the market does.  Secondly, we are geographically unconstrained; this means our deliver-ers go to where the action is and are reactive.  This means we can address the full Manhattan TAM, not just a section of it because we're afraid we cannot handle the full island.  Third, the system encourages proactive ordering since the early bird gets the worm.  The market constrains our supply, which should initiate a virtuous circle and help drive demand.  

#### features
* Non-deterministic (Eateasy doesn't have to choose) 
* Responsive to customer randomness (First come first serve)
* Geographically unconstrained delivery (cost of carry of supply is the only constraint) 
* Market driven (the customers constrain their own demand)
* Encourages clustering (save delivery costs)

### how it works
All slots are inactive unless the algo enforces a boolean ```True```. 

1. Customer places an order 
2. Iterate through all delivery slots by calling ```dynamicClusteringEngine(SlotCollection, NewOrder)``` or move onto the next slot.  Attempts to enforce ```True``` are made for each slot 
3. Customer chooses from active (```True```) slots
4. Customer order is added to their chosen slot
5. Repeat for a new customer order

### ux notes
Users see only a list of hours and can select only those that are active.  Behind the scenes however that hourly slot is composed of a number of (hour, car) (rows, columns).  That hourly slot is active if the any (hour, car)/(row, column) in the row is active (e.g., an hour is active if *any* (car)/(column) is active on that row).  An hour is inactive if *all* (cars)/(columns) in the row are in inactive.

### files
* *algo.py*: main dynamic clustering engine algo
* *order.py*: order object, inherits from models/python
* *deliveryslot.py*: delivery slot object that holds a list of orders
* *slotcollection.py*: 2D container object of deliveryslots

### in action
First instantiate a slotcollection, passing first the row slots (delivery hours), second the columns (delivery cars):

```python
newSlotCollection = slotcollection.SlotCollection(12,2)
```

Second add some orders to the ```newSlotCollection```.  Here we're adding a new order to the slot corresponding to the 8th hour and the 2nd car.  If delivery hours begin at, say, 11AM, then the 8th hour is actually 7PM.
```python
newSlotCollection.addOrderToSlot(8, 2, order.Order("123 Main Street")
```
Third pass the new customer order to the algo:
```python
dynamicClusterEngine(newSlotCollection, newUserOrder)
```

Fourth post-algo expose the Active parameter of all Slots in the Slot Collection, sample JSON output:
```json
{
    "Active": "True",
    "Car": "1",
    "Hour": "10",
    "NumOrders": "2",
    "Orders": "[\"123 Main St\", \"123 Line Ave\"]"
}
```
You can also output the active/inactive attributes of the entire ```SlotCollection``` with ```newSlotCollection.outputCollectionActive()```:
```text
[[1, False, False],
 [2, True, True],
 ...
 ...
 [12, True, True]]
```

### formatting methods on slots 
All calls made to a ```SlotCollection``` object are made with ```hours``` first and ```cars``` second.  ```hours``` correspond to ```row``` lists and ```cars``` correspond to row-list elements (columns). 

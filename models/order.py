import mongo
import pymongo
import arrow
from bson.objectid import ObjectId
from util.utilities import iso_string_to_datetime, datetime_to_iso_string
from datetime import datetime
import random


class OrderDAO():
    _collection = mongo.db()["Order"]

    def findByDates(self, date):
        try:
            parsed = arrow.get(date)
            minDate = parsed.floor("day")
            maxDate = parsed.ceil("day")
            dateQuery = {"$lte": maxDate.datetime, "$gte": minDate.datetime}
            temp = iso_string_to_datetime(date)
            query = {"deliveryDates.date": dateQuery}
            order = self._collection.find(query)
            return order
        except Exception as inst:
            print inst
            return None


class Order(object):
    def __init__(self, address, car):
        self.address = address
        self.dummyDistance = random.uniform(0, 8)
        self.car = car

    def getDistance(self, Order):
        """
            Implement Google Maps API here
        """
        return self.dummyDistance


class NewOrder(object):
    def __init__(self, address):
        self.address = address
        self.dummyDistance = random.uniform(0, 8)

    def getDistance(self, Order):
        """
            Implement Google Maps API here
        """
        return self.dummyDistance

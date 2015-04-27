import mongo
import pymongo
import arrow
from bson.objectid import ObjectId
from util.utilities import iso_string_to_datetime, datetime_to_iso_string
from datetime import datetime


class Order():
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
            return list(order)
        except Exception as inst:
            print inst
            return None

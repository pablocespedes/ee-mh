from datetime import datetime
from flask import make_response
import json
import time
from bson.objectid import ObjectId
from pymongo.cursor import Cursor
_date_format = "%Y-%m-%dT%H:%M:%S.%fZ"
import arrow
from json import JSONEncoder


class MongoEncoder(JSONEncoder):
    def default(self, obj, **kwargs):
        if isinstance(obj, ObjectId):
            return str(obj)
        if isinstance(obj, datetime):
            return datetime_to_iso_string(obj)
        if isinstance(obj, Cursor):
            return list(obj)
        else:
            return JSONEncoder.default(obj, **kwargs)


def iso_string_to_datetime(iso_string_date):
    return datetime.strptime(iso_string_date, _date_format)


def datetime_to_iso_string(dateTime):
    return dateTime.strftime(_date_format)


def output_json(obj, code, headers=None):
    """
    This is needed because we need to use a custom JSON converter
    that knows how to translate MongoDB types to JSON.
    """
    if isinstance(obj, Cursor):
        resp = make_response(json.dumps(list(obj), cls=MongoEncoder), code)
    else:
        resp = make_response(json.dumps(obj, cls=MongoEncoder), code)

    resp.headers.extend(headers or {})

    return resp


def jsonObjectType(value):
    if isinstance(value, dict):
        return {jsonObjectType(key): jsonObjectType(value) for key,
                value in value.iteritems()}
    elif isinstance(value, list):
        return [jsonObjectType(element) for element in value]
    elif isinstance(value, unicode):
        return value.encode('utf-8')
    else:
        return value

def utc2eastern (utc):
    arr = arrow.get(utc)
    eastern = arr.to('US/Eastern')
    return eastern.datetime

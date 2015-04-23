from pymongo import MongoClient
import settings


class Connection():
    con = None

_con = Connection()


def initial_connection():
    if _con.con is None:
        _con.con = MongoClient(settings.mongo_uri, tz_aware=True)
    return _con.con


def db():
    return initial_connection()[settings.mongo_db_name]

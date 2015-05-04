import settings
import deliveryalgo.algo
from flask import Flask
from flask.ext import restful
from flask.ext.cors import CORS
from flask.ext.restful import reqparse, abort, Api, Resource
from models.order import OrderDAO
from models.order import Order
from models.order import NewOrder
from util import utilities
from deliveryalgo.slotcollection import SlotCollection

app = Flask(__name__)
cors = CORS(app)
api = restful.Api(app)


def toOrder(order):
    return Order(order["address"], order.get("car", 1))


class AlgoResource(restful.Resource):
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument("startDate", type=str, required=True)
        parser.add_argument("endDate", type=str, required=True)
        args = parser.parse_args()
        print args
        try:
            startDate = utilities.iso_string_to_datetime(args.startDate)
            endDate = utilities.iso_string_to_datetime(args.endDate)
            sc = SlotCollection(11, 2)
            _order = OrderDAO()
            orders = _order.findByDates(startDate, endDate)
            mapped = map(toOrder, orders)
            for o in mapped:
                sc.addOrderToSlot(2, o.car, o)
            newUserOrder = NewOrder("315 East 21st")
            deliveryalgo.algo.dynamicClusteringEngine(sc, newUserOrder)
            temp = self.pretty(sc.collectionActive())
            return temp
        except Exception as inst:
            print inst
            return {'error': 'parsing the dates or getting the data'}

    def pretty(self, list):
        def add(x, y):
            x.append({"slot": y[0], "cars": {"one": y[1], "two": y[2]}})
            return x
        return reduce(add, list, [])


api.add_resource(AlgoResource, '/')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=settings.port, debug=True)

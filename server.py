from flask import Flask
from flask.ext.cors import CORS
import settings
from models.order import Order


app = Flask(__name__)
cors = CORS(app)


@app.route('/')
def hello_world():
    _order = Order()
    try:
        print _order.findByDates("2015-03-27T01:00:00.000Z")
        return "Works"
    except Exception as inst:
        print inst
        return "Error"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=settings.port)

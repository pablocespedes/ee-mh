from flask import Flask
from flask.ext.cors import CORS
import settings


app = Flask(__name__)
cors = CORS(app)


@app.route('/')
def hello_world():
    return 'Hello World!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=settings.port)

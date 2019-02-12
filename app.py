from flask import Flask ,jsonify
import requests

req = requests.get()

app = Flask(__name__)


@app.route('/')
def hello_world():
    return jsonify({"nombre":"pedro"},{"apellido":"fernandez"})


if __name__ == '__main__':
    app.run()

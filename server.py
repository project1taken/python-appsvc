from flask import Flask, request
from flask_restful import Resource, Api
from sqlalchemy import create_engine
from json import dumps
from flask.ext.jsonpify import jsonify
import random

app = Flask(__name__)
class appid_class:
    def get_now(self):
        number_array=[0]
        for x in range(10):
            number_array.append(random.randint(0,9))
        number_string=''.join(map(str, number_array))
        print(number_string)
        return number_string

@app.route('/c')
def index():
    return_number=appid_class()
    btest=return_number.get_now()
    return btest

if __name__ == '__main__':
    app.run(port=5000)

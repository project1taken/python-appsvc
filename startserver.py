from flask import Flask, request
from flask_restful import Resource, Api
from sqlalchemy import create_engine
from json import dumps
from flask.ext.jsonpify import jsonify
import random

#e = create_engine('sqlite:///appid.db')

app = Flask(__name__)
api = Api(app)

class generate_appid:
    def get_now(self):
        number_array=[0]
        for x in range(10):
            number_array.append(random.randint(0,9))
        number_string=''.join(map(str, number_array))
        #print number_string
        return number_string
class appid(Resource):
    def get(self):
        number_initialise = generate_appid()
        appid1=number_initialise.get_now()
#        conn = e.connect()
#        conn.execute("insert into APPID (ID) values (%d)" %int(appid1))
        return {'appid': appid1 }
api.add_resource(appid, '/appid')
#api.add_resource(appid, '/')
if __name__=='__main__':
    app.run(host="0.0.0.0", port=5000)
    

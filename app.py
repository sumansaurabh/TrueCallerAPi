import os
from tcapi.TrueCallerApp.caller import HealthCheck
from tcapi.TrueCallerApp.modules.TrueCallerInit.TrueCaller import TrueCaller
from tcapi.TrueCallerApp.caller import Caller

from flask import Flask
from flask_restful import Api



app = Flask(__name__)

api = Api(app, prefix='/v1', catch_all_404s=True)

app.config.from_object(os.environ['TCAPP_SETTINGS'])

# Initializing TrueCaller Module
trueCaller= TrueCaller()
    
#Rounting
api.add_resource(Caller, '/location/<string:location>/number/<string:number>', resource_class_kwargs={'trueCaller':trueCaller})
api.add_resource(HealthCheck, '/healthcheck')


if __name__ == '__main__':
    trueCaller.initializeLogin()
    app.run(host='0.0.0.0', port=int(os.environ['TCAPP_PORT']))

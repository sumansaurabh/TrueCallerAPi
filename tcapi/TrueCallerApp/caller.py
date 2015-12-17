'''
Created on 18-Dec-2015

@author: Suman Saurabh
'''

"""
/v1/users/ endpoint
"""

from flask_restful import Resource
from tcapi.TrueCallerApp.models.ResponseModel import ResponseModel
from tcapi.TrueCallerApp.controllers.controllers import Controller


class BaseCaller(Resource):
    """This is Base Caller"""

# Health Check class    
class HealthCheck(BaseCaller):
    def get(self):
        return "Healthy"

# Handles the REST call
class Caller(BaseCaller):
    
    def __init__(self, **kwargs):
        self.trueCaller=kwargs['trueCaller']
    
    def get(self, location, number):
        
        """      
        if location is None:
            return ResponseModel( status_code = 400, data = "Invalid Location", status = "error").__dict__
            #return ResponseModel( )
        if number is None:
            return  ResponseModel( status_code = 400, data = "Invalid Number", status = "error").__dict__
        """    
        trueCallerController=Controller(self.trueCaller)
        trueCallerController.setUrl(location, number)
        callerName = trueCallerController.getTrueCallerData()
        if callerName == "The truth is out there":
            return  ResponseModel( status_code = 404, data = "Not Found", status = "error").__dict__
        
        return  ResponseModel( status_code = 200, data = callerName, status = "success").__dict__
        

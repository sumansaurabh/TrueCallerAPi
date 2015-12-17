"""Models for Reposne"""

class ResponseModel():

    
    def __init__(self, status, status_code, data):
        self.status = status
        self.status_code = status_code
        self.name = data
    

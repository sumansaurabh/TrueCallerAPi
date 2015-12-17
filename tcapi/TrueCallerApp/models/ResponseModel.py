'''
Created on 18-Dec-2015

@author: Suman Saurabh
'''

"""Models for Reposne"""

class ResponseModel():

    
    def __init__(self, status, status_code, data):
        self.status = status
        self.status_code = status_code
        self.name = data
    

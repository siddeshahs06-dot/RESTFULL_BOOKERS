import requests 
from utils.config_reader import BASE_URL 

class APLClient: 
    def get_user(self, END_POINT): 
        return requests.get(BASE_URL + END_POINT) 
    
    def post_user(self,END_POINT,payload,headers): 
        return requests.post(BASE_URL + END_POINT, json=payload, headers=headers) 
    
    def get_user_byid(self,END_POINT,headers):
        return requests.get(BASE_URL + END_POINT,headers=headers)
    
    def put_user(self,END_POINT,headers,payload,auth):
        return requests.put(BASE_URL+END_POINT,headers=headers,json=payload,auth=("admin","password123"))
        
apiclient=APLClient()
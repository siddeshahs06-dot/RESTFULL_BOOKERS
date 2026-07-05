import requests
from utils.config_reader import BASE_URL
from api.api_client import apiclient

#BASE_URL="https://restful-booker.herokuapp.com"
END_POINT="/ping"
END_POINT1="/auth"
END_POINT2="/booking"
token=" "
headers={"Contetnt-Type":"application/json",
            "Accept" : "application/json",
             "cookie": f"token={token}" }


def test_health_checkup():
    
    #url=BASE_URL+END_POINT
    response=apiclient.get_user(END_POINT)

   # print(response.json())

    assert response.status_code == 201

'''    
def test_create_token():
    url=BASE_URL+END_POINT1
    
    payload={
        "username":"admin",
        "password":"password123"
    }
    response=requests.post(url,headers=headers,json=payload)
    print(response.json()["token"])
    
    assert response.status_code == 200
   # assert "token" in response.json()
    return response.json()["token"]

token=test_create_token()
print(token) 
'''

def test_Create_booking():
    url=BASE_URL+END_POINT2
    payload={
    "firstname":"siddu",
    "lastname":"hs",
    "totalprice":600,
    "depositpaid":False,
    "bookingdates":{
        "checkin":"2026-07-04",
        "checkout":"2026-07-05"
    },
    "additionalneeds":"Lunch"
    }
    
    response=apiclient.post_user(END_POINT2,payload,headers)
    print(response.json())

    assert response.status_code == 200
    return response.json()["bookingid"]

booking_id=test_Create_booking()
booking_id=str(booking_id)
print(type(booking_id))


def test_booking_id():
    #url=BASE_URL+END_POINT2

    response=apiclient.get_user(END_POINT2)
    print(response.json())

    assert response.status_code == 200


def test_get_book_by_id():
    #url=BASE_URL+END_POINT2+"/"+booking_id
    END_POINT12=END_POINT2+"/"+booking_id
    

    response=apiclient.get_user_byid(END_POINT12,headers)
    #print(response.json()["bookingid"])

    assert response.json()["firstname"] == "siddu"
    assert response.json()["lastname"] == "hs"
    assert response.json()["depositpaid"] == False
    #print(response.json()[booking_id])

 
 
 

def test_Update_Booking():
    auth={
        "username":"admin",
        "password":"password123"
    }
    payload={
        "firstname":"ramesh",
    "lastname":"ram",
    "totalprice":500,
    "depositpaid":False,
    "bookingdates":{
        "checkin":"2026-07-01",
        "checkout":"2026-07-10"
    },
    "additionalneeds":"Breakfast"
    }
    END_POINT=END_POINT2+"/"+booking_id

    response=apiclient.put_user(END_POINT,headers,payload,auth)
    
    assert response.status_code == 200 
    assert response.json()["firstname"] == "ramesh"







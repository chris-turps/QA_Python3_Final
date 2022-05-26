import json
import requests

class User:
    def __init__(self
        , name_txt
        , pwd_txt
    ):
        self.name = name_txt
        self.pwd = pwd_txt

chris_obj = User("christ", "password123")
eddie_obj = User("eddieP", "admin123")
# 
# userList = [chris_obj, eddie_obj]
# print(userList)
# userTypes = [user.name for user in userList]
# print(userTypes)
# print(chris_obj.name)

def nxapi_post(url, myheaders, payload, switchuser, switchpassword):
    response = requests.post(url, data=json.dumps(payload), headers=myheaders, auth=(switchuser, switchpassword)).json()
    print(response)
    
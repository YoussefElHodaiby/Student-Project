from pickle import GLOBAL

import pytest
import requests
import json
import os
import random

base_url = "http://localhost:8082/students"



names = ["hady", "mahmoud", "omar", "zein", "mourad","ismail","ahmed", "aly", "yehia"]
random_name = random.choice(names)

request_payload = {


        "name":random_name,
        "age":35

}

def test_get_validation():
    response = requests.get(base_url)
    print(response.text)
    assert response.status_code == 200




def test_post_validation():
    response = requests.post(base_url, json=request_payload)

    data = response.json()
    recieved_id = data["id"]
    recieved_name=data["name"]
    print("new id is "+str(recieved_id))


    print(response.text)
    assert response.status_code == 201
    assert random_name==recieved_name

    return recieved_id




def test_get_validation2():
    response = requests.get(base_url+"/"+str(test_post_validation()))
    print(response.text)
    assert response.status_code == 200

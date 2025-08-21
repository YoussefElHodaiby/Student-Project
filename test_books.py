import pytest
import requests
import json
import os
import random

base_url = "http://localhost:8082/api/books"

request_payload = {
    "bookName": "NEW"
}

def test_get_books():
    response = requests.get(base_url)
    print(response.text)
    assert response.status_code == 200

def test_get_books_byid():
    response = requests.get(base_url + "/3")
    print(response.text)
    assert response.status_code == 200

def test_post_books():
    response = requests.post(base_url, json=request_payload)
    print(response.text)
    assert response.status_code == 200 or response.status_code == 201


def test_put_single_book():
    response = requests.post(base_url + "/3", json=request_payload)
    print(response.text)
    assert response.status_code == 200 or response.status_code == 201

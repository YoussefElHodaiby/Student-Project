"""
Legacy API testing script - consider using test_student_api.py for proper testing
"""
import requests
import random

# Test data
names = ["hady", "mahmoud", "omar", "zein", "mourad", "ismail", "ahmed", "aly", "yehia"]
random_name = random.choice(names)

updates_names = ["ahmed", "aly", "yehia", "khaled", "ismail"]
random_updates_names = random.choice(updates_names)

updates_age = [25, 30, 35, 40, 45]  # Changed from strings to integers
random_updates_age = random.choice(updates_age)





# Payload for creating student
request_payload = {
    "name": random_name,
    "age": 35
}

# Payload for updating student
request_payload_update = {
    "name": random_updates_names,
    "age": random_updates_age,
}

# Create student
response = requests.post("http://localhost:8082/students", json=request_payload)
print(f"Create Status Code: {response.status_code}")
print(f"Create Response: {response.text}")

data = response.json()
received_id = data["id"]
received_name = data["name"]

# Get student
response_get = requests.get(f"http://localhost:8082/students/{received_id}")
print(f"Retrieved ID: {received_id}")
print(f"Retrieved Name: {received_name}")

# Fixed assertion - this was always True before
assert received_name == request_payload["name"]  # Verify the name matches what we sent


# Update student
response_update = requests.put(f"http://localhost:8082/students/{received_id}", 
                              json=request_payload_update)

data_updated = response_update.json()
received_id_updated = data_updated["id"]
received_name_updated = data_updated["name"]

if received_name_updated == received_name:
    print("Names are the same")
else:
    print("Names are different - update successful")

print(f"Update Response: {response_update.text}")
print(f"Updated Name: {received_name_updated}")
print(f"Updated ID: {received_id_updated}")

# Fixed assertion - verify the update actually worked
assert received_name_updated == request_payload_update["name"]



# Delete student
response_delete = requests.delete(f"http://localhost:8082/students/{received_id}")
print(f"Delete Status Code: {response_delete.status_code}")

# Test getting non-existent student (should return 404)
response_404 = requests.get("http://localhost:8082/students/100")
print(f"Non-existent Student Status Code: {response_404.status_code}")
assert response_404.status_code == 404  # Should be 404 for non-existent resource





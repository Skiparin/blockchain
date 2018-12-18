import requests
import json

requests.post("http://localhost:5001/transactions/new", 
	json={"from":"Hans","to":"Emil","message":"Hello Emil"})

response = requests.get("http://localhost:5002/transactions/get").json()

print("Transaction:")
print(json.dumps(response, indent=4))

requests.post("http://localhost:5001/transactions/new", 
	json={"from":"Emil","to":"Hans","message":"Hello Hans"})

requests.post("http://localhost:5001/mine")

response = requests.get("http://localhost:5001/chain/get").json()

print("Chain:")
print(json.dumps(response, indent=4))


requests.get("http://localhost:5004/delete_info")


response = requests.get("http://localhost:5004/chain/get").json()

print("Empty:")
print(json.dumps(response, indent=4))


requests.post("http://localhost:5004/join_network", json={"connection": "http://192.168.0.1:5001"})


response = requests.get("http://localhost:5004/chain/get").json()

print("Back on chain:")
print(json.dumps(response, indent=4))
import requests

url = "http://127.0.0.1:8001/predict/"

# Dummy input (78 features)
data = {
    "features": [0]*78
}

response = requests.post(url, json=data)

print("Status:", response.status_code)
print("Response:", response.json())
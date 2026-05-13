import requests
import time
import numpy as np

# API endpoint
URL = "http://127.0.0.1:8001/predict/"

# Load real dataset
X = np.load("data/processed/X_test.npy")

print("✅ Loaded dataset:", X.shape)

i = 0

while True:
    sample = X[i].tolist()

    response = requests.post(URL, json={
        "features": sample
    })

    try:
        print(response.json())
    except:
        print("Error:", response.text)

    i += 1

    if i >= len(X):
        i = 0  # loop again

    time.sleep(1)  # 1 sec delay
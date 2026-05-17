from ids_app.utils import predict

# Fake feature vector
features = [0.5] * 78

result = predict(features)

print(result)
import requests

api = "http://jservice.io/api/random"

print(requests.get(api))
print(requests.get(api).json())
print("\n\n")
print(requests.get(api).json()[0])
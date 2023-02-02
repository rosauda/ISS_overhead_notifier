import requests

# International space station current location
response = requests.get(url="http://api.open-notify.org/iss-now.json")

print(response)


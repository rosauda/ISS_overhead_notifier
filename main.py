import requests
from datetime import datetime
import mpu

# ---------------------------- CONSTANTS ------------------------------- #

MY_LAT = 53.551086
MY_LOG = 9.993682

# ---------------------------- GETTING ISS CURRENT POSITION USING API ------------------------------- #

# International space station current location
response = requests.get(url="http://api.open-notify.org/iss-now.json")

# Raising errors and exceptions
response.raise_for_status()

# Getting ISS current location - latitude and longitude
iss_longitude = float(response.json()["iss_position"]["longitude"])
iss_latitude = float(response.json()["iss_position"]["latitude"])

# ---------------------------- GETTING MY LOCATION SUNSET AND SUNRISE HOUR USING API ------------------------------- #

# Sunset and sunrise times API
parameters = {
    "let": MY_LAT,
    "lng": MY_LOG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)

# Raising errors and exceptions
response.raise_for_status()

# Getting sunrise and sunset time in my location. Extracting hour
data = response.json()
sunrise_hour = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset_hour = int(data["results"]["sunset"].split("T")[1].split(":")[0])


# Time now. extracting hour
time_now = datetime.now()
hour_now = int(time_now.hour)


# ---------------------------- CHECKING CONDITIONS TO SEND EMAIL ------------------------------- #
# Conditions to be checked
# 1. My location needs to be dark
# 2. The distance between my location and the ISS locations <= 400km

# Calculating distance between my location and ISS in km
distance = mpu.haversine_distance((iss_latitude, iss_longitude), (MY_LAT, MY_LOG))

# If conditions are matched, send email
if sunset_hour <= hour_now <= sunrise_hour and distance <= 400:
    send_email = True
else:
    send_email = False

# ---------------------------- SENDING EMAIL ------------------------------- #











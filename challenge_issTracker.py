#!/usr/bin/env python3
"""Returning the location of the ISS in latitude/longitude"""
import requests
import datetime
import reverse_geocoder as revgeo

URL= "http://api.open-notify.org/iss-now.json"
def main():
    resp= requests.get(URL).json()

    #Api changes each time a GET request is sent 
    lon = resp["iss_position"]["longitude"]
    lat = resp["iss_position"]["latitude"]
    epoch_time = resp["timestamp"]
    
    location_resp = revgeo.search((lat, lon))

    city = location_resp[0]["name"]

    country = location_resp[0]["cc"]

    date_time = datetime.datetime.fromtimestamp(epoch_time)

    print(f"""CURRENT LOCATION OF THE ISS:
    Timestamp: {date_time}
    Lon: {lon}
    lat: {lat}
    City/Country: {city}, {country}
    """)

if __name__ == "__main__":
    main()

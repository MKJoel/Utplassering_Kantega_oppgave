"""
from fastapi import FastAPI
import requests
import xml.etree.ElementTree as ET

app=FastAPI()
tree = ET.ElementTree

#vettafaan
url = "https://api.met.no/weatherapi/locationforecast/2.0/classic?"
setLatitude = "lat=59.93"
setLongitude = "&lon=10.72"
setAltitude = "&altitude=90"

@app.get("/")
    async def magic():
        url = ("https://api.met.no/weatherapi/locationforecast/2.0/classic?",setLatitude,setLongitude,setAltitude)
        response = requests.get(url)
        return response.json()
"""

# her importerer jeg bibliotekene fast API og requests
from fastapi import FastAPI
import requests

#FastAPI gjør en GET request, deretter kjører ned funksjonen "magic"
app = FastAPI()
@app.get("/")
async def magic():
    url = f"https://api.met.no/weatherapi/locationforecast/2.0/compact?lat=63.446827&lon=10.421906&altitude=90"
    #headers forteller API'et hvem som spørr etter informasjon, noe som var et krav for API'et
    headers = {'User-Agent': 'YourApp/1.0'} 
    #response gjør en HTTP GET request, og får da daten, dataen kan hentes ut med en .json funksjon.
    response = requests.get(url, headers=headers)
    json = response.json()

    #her velger vi dataen vi vil hente ut
    data = {
    'temperature': json['properties']['timeseries'][0]['data']['instant']['details']['air_temperature'],
    'next_6_hours': json['properties']['timeseries'][0]['data']['next_6_hours']['summary']['symbol_code']
}
    return data

    """
    weather_data = []
    for timeseries in data['properties']['timeseries']:
        if 'next_6_hours' in timeseries['data']:
            weather_data.append({
                "next_6_hours": timeseries['data']['next_6_hours'],
                "air_temperature": timeseries['data']['instant']['details']['air_temperature'],
                "symbol_code": timeseries['data']['next_6_hours']['summary']['symbol_code']
            })
    
    """

    







"""@app.get("/")
async def root():
    url = "https://api.met.no/weatherapi/locationforecast/2.0/classic?lat=59.93&lon=10.72&altitude=90"
    response = requests.get(url)
    xml_root = ET.fromstring(response.content)
    response = requests.get(url)

    flights = []
    for flight in xml_root.findall(".//weather"):
        flights.append({
            "flightid": flight.find("flight_id").text,
            "scheduletime": flight.find("schedule_time").text
        })
    
    return {"flights": flights}
"""


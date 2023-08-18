from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut
import time

f = open("address.txt", "r")
# print(f.readlines()) 

def do_geocode(address):
    geolocator = Nominatim(user_agent="Vivek")
    try:
        return geolocator.geocode(address)
    except GeocoderTimedOut:
        return do_geocode(address)

for line in f.readlines():
    location = do_geocode(line)
    print(location.address)
    print((location.latitude, location.longitude))
    time.sleep(15)


AIzaSyBMvo2sN-QeEjT163b4hLG_HLKpqA0JItY

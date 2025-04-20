import phonenumbers
from phonenumbers import geocoder
from phonenumbers import carrier
from opencage.geocoder import OpenCageGeocode
import folium

number = input("Phone Number to Search (with Country Code): ")

pepNumber = phonenumbers.parse(number)
location = geocoder.description_for_number(pepNumber, "en")

service_pro = phonenumbers.parse(number)

key = "425bd4e2203b413b9c15c3697102e25f"

geocoder = OpenCageGeocode(key)
query = str(location)
results = geocoder.geocode(query)

lat = results[0]["geometry"]["lat"]
lng = results[0]["geometry"]["lng"]

print("\n" + location)


print(carrier.name_for_number(service_pro, "en"))


print(f"\nLatitude: {lat}\nLongitude: {lng}")

myMap = folium.Map(location=[lat, lng], zoom_start=9)
folium.Marker([lat, lng], popup=location).add_to(myMap)

myMap.save("countryLocation.html")

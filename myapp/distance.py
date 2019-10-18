from geopy.geocoders import Nominatim
from geopy.distance import geodesic

geolocator = Nominatim(user_agent="myapp")
location = geolocator.geocode("175 5th Avenue NYC")
casa = (-3.7255366,-38.5571957)
casapais = (-3.7272136,-38.5665047)
print(geodesic(casa, casapais).km)
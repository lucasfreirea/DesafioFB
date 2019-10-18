from rest_framework import serializers
from .models import Establishment
from geopy.geocoders import Nominatim
from geopy.distance import geodesic

class EstablishmentSerializer(serializers.ModelSerializer):

    dist = serializers.SerializerMethodField()

    class Meta:

        model = Establishment
        fields = '__all__'

    def get_dist(self, obj):
        print(self.context['request'].GET.dict().get('lat'))
        print(self.context['request'].GET.dict().get('lng'))
        geolocator = Nominatim(user_agent="myapp")
        return geodesic((obj.lat,obj.lng), (-3.72796552, -38.55526865)).km
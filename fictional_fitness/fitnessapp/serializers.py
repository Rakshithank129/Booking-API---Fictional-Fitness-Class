from rest_framework import serializers
from fitnessapp.models import FitnessClass,Booking

class FitnessClassSerializers(serializers.ModelSerializer):
    class Meta:
        model = FitnessClass
        fields = '__all__'

class BookingSerializers(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'

class BookingRequestSerializer(serializers.Serializer):
    class_id = serializers.IntegerField()
    client_name = serializers.CharField()
    client_email = serializers.EmailField()

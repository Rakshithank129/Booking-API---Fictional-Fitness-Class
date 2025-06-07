from django.shortcuts import render
from fitnessapp.models import FitnessClass,Booking
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from fitnessapp.serializers import FitnessClassSerializers,BookingSerializers,BookingRequestSerializer

# Create your views here.

def home(request):
    classes = FitnessClass.objects.all()
    return render(request,'home.html',{'classes':classes})

class FitnessClassListView(APIView):
    def get(self,request):
        classes = FitnessClass.objects.all()
        serializer = FitnessClassSerializers(classes,many=True)
        return Response(serializer.data)


class BookClassView(APIView):
    def post(self,request):
        serializer = BookingSerializers(data=request.data)
        if serializer.is_valid():
            class_id = serializer.validated_data['class_id']
            client_name = serializer.validated_data['client_name']
            client_email = serializer.validated_data['client_email']

            try:
                fitness_class = FitnessClass.objects.get(id = class_id)
            except FitnessClass.DoesNotExist:
                return Response({"error":"class not found"},status=status.HTTP_404_NOT_FOUND)
            
            if fitness_class.available_slots <=0:
                return Response({"error":"No available slots"},status=status.HTTP_400_BAD_REQUEST)
            
            Booking.objects.create(fitness_class=fitness_class,client_name=client_name,client_email=client_email)
            fitness_class.available_slots -=1
            fitness_class.save()

            return Response({"message":"Booking Successfull"},status=status.HTTP_200_OK)
        
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
class BookingListView(APIView):
    def get(self,request):
        email = request.query_params.get('email')
        if not email:
            return Response({"error":"email is required"},status=status.HTTP_400_BAD_REQUEST)
        
        Bookings = Booking.objects.filter(client_email=email) 
        serializer = BookingSerializers(Bookings,many=True)
        return Response(serializer.data)
    
    

        

    

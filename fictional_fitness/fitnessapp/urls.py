from django.urls import path
from fitnessapp.views import home,FitnessClassListView,BookingListView,BookClassView

urlpatterns = [
    path('',home,name='home'),
    path('classes/',FitnessClassListView.as_view(),name='fitness-class-list'),
    path('book/',BookClassView.as_view(),name='book-class'),
    path('bookings/',BookingListView.as_view(),name='booking-list'),

]

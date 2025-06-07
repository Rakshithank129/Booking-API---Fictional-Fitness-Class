from django.db import models

# Create your models here.
class FitnessClass(models.Model):
    name = models.CharField(max_length=150)
    instructor = models.CharField(max_length=150)
    date_time = models.DateTimeField()
    time_slots = models.IntegerField()
    # start_time = models.TimeField()
    # end_time = models.TimeField(default="09:00:00")
    available_slots = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.name} - {self.date_time}"                  
    
class Booking(models.Model):                       
    fitness_class = models.ForeignKey(FitnessClass,on_delete=models.CASCADE)         
    client_name = models.CharField(max_length=150)
    client_email = models.EmailField()

    def __str__(self):
        return f"{self.client_name} - {self.fitness_class.name}"      




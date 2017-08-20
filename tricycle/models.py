from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.core.urlresolvers import reverse
# Create your models here.
class Operator(models.Model):
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=1)
    address = models.CharField(max_length = 300)
    date_registered = models.DateField()  
    contact_number = models.CharField(max_length = 15)
    image = models.FileField()  
    def __str__(self):
        return self.first_name+" "+self.last_name
    def get_absolute_url(self):
        return reverse('tricycle:details',kwargs={'pk':self.pk})


class Driver(models.Model):
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=1)
    address = models.CharField(max_length = 300)
    date_registered = models.DateField()
    contact_number = models.CharField(max_length = 15)
    image = models.FileField() 
    def __str__(self):
        return str(self.id)+" "+self.first_name+" "+self.last_name
    def get_absolute_url(self):
        return reverse('tricycle:driver-details',kwargs={'pk':self.pk})
    
    


class Tricycle(models.Model):
    operator = models.ForeignKey(Operator,on_delete=models.CASCADE)
    body_number = models.IntegerField(unique = True,
                                      validators=[
                                          MaxValueValidator(1000),
                                          MinValueValidator(1)
                                          ])
    date_registered = models.DateField()
    driver = models.OneToOneField(
        Driver,
        on_delete=models.SET_NULL,
        null=True,
    )
    def __str__(self):
        return str(self.body_number)
    def get_absolute_url(self):
        return reverse('tricycle:tricycle-details',kwargs={'pk':self.pk})
        
    

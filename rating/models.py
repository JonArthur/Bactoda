from django.db import models
from tricycle import models as tricyle_models
# Create your models here.
class Rate(models.Model):
	name = models.CharField(max_length=100)
	comment = models.TextField(max_length=1000)
	driver = models.ForeignKey(tricyle_models.Driver,on_delete = models.CASCADE)
	email = models.CharField(max_length = 200)
	def get_absolute_url():
		return reverse('raiting:rate',kwargs={'pk':self.pk})
	def __str__(self):
		return self.driver.first_name+" "+str(self.id)
	
		
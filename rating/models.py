from django.db import models
from tricycle import models as tricyle_models
from django.core.urlresolvers import reverse
# Create your models here.
class Rate(models.Model):
	name = models.CharField(max_length=100)
	comment = models.TextField(max_length=1000)
	driver = models.ForeignKey(tricyle_models.Driver,on_delete = models.CASCADE)
	rating = models.IntegerField()
	email = models.CharField(max_length = 200)
	
	def get_absolute_url(self):
		return reverse('rating:index')
	def __str__(self):
		return self.driver.first_name+" "+str(self.id)
	
		
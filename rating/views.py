from django.shortcuts import render,get_object_or_404
from tricycle.models import Driver,Tricycle
from django.http import HttpResponse
from django.views.generic.edit import CreateView
from django.views.generic import ListView
from .forms import RateForm
from .models import Rate
from tricycle.models import Driver
import datetime
class RateCreateView(CreateView):
	model = Rate
	form_class = RateForm
class IndexView(ListView):
	# query = request.Get.get("query")
	template_name = 'rating/index.html'
	def get_queryset(self):
		return Driver.objects.all() 

def current_datetime(request):
    now = datetime.datetime.now()
    query = request.POST.get("query")
    tric = get_object_or_404(Tricycle,body_number = int(query))
    driver = tric.driver
    rating = driver.rate_set.all()
    html = "<html><body>It is now %s.<br>	</body></html>" % query
    return render(request, 'rating/detail.html', {
            'driver': tric,
            'ratings':rating,
            })
   
# def index(request):
#     driver = Driver.objects.all()
#     output = ', '.join([q.first_name for q in driver])
#     return HttpResponse(output)

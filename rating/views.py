from django.shortcuts import render,get_object_or_404,redirect
from tricycle.models import Driver,Tricycle
from django.http import HttpResponse
from django.views.generic.edit import CreateView
from django.views.generic import ListView
from .forms import RateForm
from .models import Rate
from tricycle.models import Driver
from django.db.models import Avg
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
    avg_rating = driver.rate_set.all().aggregate(Avg('rating'))
    return render(request, 'rating/detail.html', {
            'driver': tric,
            'ratings':rating,
            'avg_rating':avg_rating,
            })

def rate(request,pk):
    form = RateForm(request.POST)
    rate = Rate()
    driver = Driver.objects.get(pk=pk)

    if request.method == 'POST':
        rate.name = request.POST.get("name")
        rate.email = request.POST.get("email")
        rate.comment = request.POST.get("comment")
        rate.rating = request.POST.get("rating")
        rate.driver = driver
        rate.save()
        return redirect('rating:index')
    return render(request, 'rating/rate_form.html', {
            'form': RateForm,
            })
    


# def index(request):
#     driver = Driver.objects.all()
#     output = ', '.join([q.first_name for q in driver])
#     return HttpResponse(output)

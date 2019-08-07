from django.shortcuts import render

from .models import Job

def home(request):
	jobs=Job.objects
	return render(request,'job/home.html',{'jobs':jobs})

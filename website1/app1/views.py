from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def func(request):
	return render(request, 'homepage.html', {'dynamic':'hey ha ha ha '})

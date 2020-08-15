from django.shortcuts import render

def index(request):
	return render(request, 'offapp/index.html')

def credits(request):
	return render(request, 'offapp/credits.html')
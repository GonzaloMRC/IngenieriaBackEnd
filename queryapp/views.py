from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Client, Car
from django.shortcuts import get_object_or_404

# Create your views here.
def hello(request, username):
    print(username)
    return HttpResponse("<h1>Hello %s</h1>" % username)

def about(request):
    return HttpResponse('About')

def clients(request):
    clients = list(Client.objects.values())
    return JsonResponse(clients, safe=False)

def cars(request, id):
    #car = Car.objects.get(id=id)
    car = get_object_or_404(Car, id=id)
    return HttpResponse('Car: %s ' % car.brand + ' ' + car.model)
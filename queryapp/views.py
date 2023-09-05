from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Client, Car, Spring, Forces, Points
from django.shortcuts import get_object_or_404
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
import json
import time
from .utils.model3d import generatePoints
from .utils.fem import fem

# Create your views here.
def hello1(request):
    return HttpResponse("<h1>Hello</h1>")

def hello(request, username):
    print(username)
    return HttpResponse("<h1>Hello %s</h1>" % username)

def about(request):
    return HttpResponse('About')

def clients(request):
    clients = list(Client.objects.values())
    return JsonResponse(clients, safe=False)

@method_decorator(csrf_exempt)
def create_client(request):
    if request.method == 'POST':
        jd = json.loads(request.body)

        if jd['name'] and jd['dni_ruc']:
            client = Client.objects.create(name=jd['name'],dni_ruc=jd['dni_ruc'], phone_number=jd['phone_number'], email=jd['email'])
            client.save()
            return JsonResponse({'message':'Client created successfully!'})
        else:
            return JsonResponse({'message':'Invalid data, Both name and dni/ruc are required.'}, status=400)
        
    return JsonResponse({'message':'POST method required.'}, status=405)

@method_decorator(csrf_exempt)
def create_spring(request):
    if request.method == 'POST':
        jd = json.loads(request.body)

        if jd['wire'] and jd['coils']:
            spring = Spring.objects.create(
                wire=jd['wire'],
                diam_ext1=jd['diam_ext1'],
                diam_ext2=jd['diam_ext2'],
                diam_int1=jd['diam_int1'],
                diam_int2=jd['diam_int2'],
                length=jd['length'],
                coils=jd['coils'],
                coil_direction=jd['coil_direction'],
                end1=jd['end1'],
                luz1=jd['luz1'],
                coils_red_1=jd['coils_red_1'],
                coils_amp_1=jd['coils_amp_1'],
                detail1_end1=jd['detail1_end1'],
                detail2_end1=jd['detail2_end1'],
                detail3_end1=jd['detail3_end1'],
                eccentricity1=jd['eccentricity1'],
                end2=jd['end2'],
                luz2=jd['luz2'],
                coils_red_2=jd['coils_red_2'],
                coils_amp_2=jd['coils_amp_2'],
                detail1_end2=jd['detail1_end2'],
                detail2_end2=jd['detail2_end2'],
                detail3_end2=jd['detail3_end2'],
                eccentricity2=jd['eccentricity2'],
                grade=jd['grade']
                )
            spring.save()
            points = generatePoints(spring)
            return JsonResponse(points, safe=False)
        else:
            return JsonResponse({'message':'Invalid data, Both wire and coils are required.'}, status=400)
        
    return JsonResponse({'message':'POST method required.'}, status=405)



def cars(request, id):
    #car = Car.objects.get(id=id)
    car = get_object_or_404(Car, id=id)
    return HttpResponse('Car: %s ' % car.brand + ' ' + car.model)
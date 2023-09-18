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

from rest_framework.decorators import api_view
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password
from django.contrib.auth.forms import UserCreationForm

def home(request):
    return render(request,'home.html')

def signup(request):

    if request.method == 'GET':
        return render(request,'signup.html', {
            'form': UserCreationForm
        })
    else:
        if request.POST['password1'] == request.POST['password2']:
            # register user
            try:
                user = User.objects.create_user(username=request.POST['username'], password=request.POST['password1'])
                user.save()
                return HttpResponse('User created successfully')
            except:
                return render(request,'signup.html', {
                    'form': UserCreationForm,
                    'error': 'Username already exists'
                })
        return render(request,'signup.html', {
            'form': UserCreationForm,
            'error': 'Password do not match'
        })
        

    

@api_view(['POST'])
def login(request):

    username = request.POST.get('username')
    password = request.POST.get('password')

    try:
        user = User.objects.get(username=username)
    except User.DoesNotExist:
        return Response("Usuario inválido")
    
    pwd_valid = check_password(password,user.password)

    if not pwd_valid:
        return Response("Contraseña inválida")

    token, created = Token.objects.get_or_create(user=user)

    print(token.key)
    return Response(token.key)


# Create your views here.

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

@method_decorator(csrf_exempt)
def simulate_spring(request):
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
            
            start_time = time.time()
            NodeX, NodeY,NodeZ, storeForceSum, storeDispl, storeStress, deform, simulations = fem(spring)

            force = Forces(
                    forces= storeForceSum,
                    displacements = [(deform + deform*j) for j in range(simulations)],
                    spring = spring
            )

            force_data = {
                'forces': list(force.forces),
                'displacements': list(force.displacements)
            }

            points=[]

            points_data = []
            
            for i in range(len(NodeX)):
                posX, posY, posZ, stress = ([] for k in range(4))
                for j in range(len(storeDispl)):
                    posX.append(NodeX[i] + storeDispl[j][i][0])
                    posY.append(NodeY[i] + storeDispl[j][i][1])
                    posZ.append(NodeZ[i] + storeDispl[j][i][2])
                    if i == len(NodeX) - 1:
                        stress.append(storeStress[j][i-1])
                    else:  
                        stress.append(storeStress[j][i])

                point = Points(posx = posX,
                                posy = posY,
                                posz = posZ,
                                esf = stress,
                                spring = spring)
                points.append(point)

                point_data = {
                    'posx': point.posx,
                    'posy': point.posy,
                    'posz': point.posz,
                    'esf': point.esf,
                }
                points_data.append(point_data)

            print(time.time() - start_time)
            
            datos={'message': 'Success', 'spring': spring.to_dict(),'points': points_data, 'forces': force_data}
            return JsonResponse(datos, safe=False)

        else:
            return JsonResponse({'message':'Invalid data, Both wire and coils are required.'}, status=400)
        
    return JsonResponse({'message':'POST method required.'}, status=405)

def cars(request, id):
    #car = Car.objects.get(id=id)
    car = get_object_or_404(Car, id=id)
    return HttpResponse('Car: %s ' % car.brand + ' ' + car.model)
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from ..queryapp.models import Client, Car, Spring, Forces, Points
from django.shortcuts import get_object_or_404
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
import json
import time
from ..queryapp.utils.model3d import generatePoints
from ..queryapp.utils.fem import fem

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
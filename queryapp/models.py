from django.db import models

# Create your models here.
class Client(models.Model):
    name = models.CharField(max_length=80)
    dni_ruc = models.CharField(max_length=11)
    phone_number = models.CharField(max_length=9)
    email = models.CharField(max_length=30)

class Car(models.Model):
    vin = models.CharField(max_length=17)
    brand = models.CharField(max_length=11)
    model = models.CharField(max_length=20)
    year = models.CharField(max_length=4)
    bodywork = models.CharField(max_length=16)
    plate = models.CharField(max_length=7)
    fuel = models.CharField(max_length=18)
    displacement = models.CharField(max_length=5)
    wheel_drive = models.CharField(max_length=9)
    gas_tank = models.CharField(max_length=14)
    net_weight = models.IntegerField()
    goss_weight = models.IntegerField()
    rows_seats = models.IntegerField()
    mileage_km = models.IntegerField()
    original_tire_code = models.CharField(max_length=9)
    installed_tire_code = models.CharField(max_length=9)
    car_use = models.CharField(max_length=18)
    extra_charge = models.CharField(max_length=25)

class SampleSpring(models.Model):
    spring_type = models.CharField(max_length=10)
    spring_position = models.CharField(max_length=9)
    suspension_type = models.CharField(max_length=16)
    coil_spacer = models.CharField(max_length=20)
    spacer_height = models.IntegerField()

    wire = models.DecimalField(max_digits=4, decimal_places=2)
    diam_ext1 = models.DecimalField(max_digits=5, decimal_places=2)
    diam_ext2 = models.DecimalField(max_digits=5, decimal_places=2)
    diam_int1 = models.DecimalField(max_digits=6, decimal_places=3, default=0)
    diam_int2 = models.DecimalField(max_digits=6, decimal_places=3, default=0)
    length = models.DecimalField(max_digits=6, decimal_places=2)
    coils = models.DecimalField(max_digits=6, decimal_places=3)
    coil_direction = models.CharField(max_length=20)
    
    
    luz1 = models.IntegerField()
    luz2 = models.IntegerField()

    
    end1 = models.CharField(max_length=50, default="-")
    red_coils1 = models.DecimalField(max_digits=6, decimal_places=3, default=0)
    
    extremo2 = models.CharField(max_length=50, default="-")
    vuelta_red2 = models.DecimalField(max_digits=6, decimal_places=3, default=0)
    grado = models.IntegerField(default=2)

class Design(models.Model):
    correlative = models.CharField(max_length=7)
    status = models.CharField(max_length=11)
    registration_date = models.DateField()
    development = models.CharField(max_length=12)
    request_reason = models.CharField(max_length=100)
    aplication = models.CharField(max_length=100)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)







from django.db import models

class Product(models.Model):
    food_id         =   models.AutoField(primary_key=True)
    food_name       =   models.CharField(max_length=128, null=False, blank=False)
    expiration_date =   models.DateField(auto_now_add=False,auto_created=False)
    location        =   models.CharField(max_length=128)
    Image           =   models.CharField(max_length=100, null=True, blank=True)

#class Meal(models.Model):
#
from django.views.generic import View
from django.shortcuts import render
from datetime import datetime
from .models import Product
from .models import Meal
from dateutil import parser


class MyPantry(View):
    def get(self, request, *args, **kwargs):
        querySet = Product.objects.all()
        temp=[]
        object_list=[]
        for i in range(len(querySet)):
            querySet[i].days_remaining = (parser.parse(str(querySet[i].expiration_date)) - datetime.now()).days
            temp.append(querySet[i])
            if (i+1)%3 == 0:
                object_list.append(temp)
                temp = []
        if len(temp)!=0:
            object_list.append(temp)
        context = {"object_list" : object_list}
        return render(request, 'myPantry.html', context)


class MyPantrySearch(View):
    def get(self, request, *args, **kwargs):
        search_string = request.GET['search_string'].strip()
        querySet = Product.objects.filter(food_name__icontains=search_string)
        temp=[]
        object_list=[]
        for i in range(len(querySet)):
            querySet[i].days_remaining = (parser.parse(str(querySet[i].expiration_date)) - datetime.now()).days
            temp.append(querySet[i])
            if (i+1)%3 == 0:
                object_list.append(temp)
                temp = []
        if len(temp)!=0:
            object_list.append(temp)
        context = {"object_list" : object_list}
        return render(request, 'myPantry.html', context)


class MyPantryAddProduct(View):
    def get(self, request, *args, **kwargs):
        food_name = request.GET['food_name'].strip()
        print("##############Just before get Expiration###############")
        food_expiry_date = request.GET['food_expiration_date'].strip()
        print("##############Just after get Expiration###############")
        food_id = Product.objects.all().count() + 1
        location = 'Fridge'
        product = Product()
        product.food_id = str(food_id)
        product.food_name = food_name
        print("##############Just before Expiration###############")
        product.expiration_date = datetime.datetime.strptime(food_expiry_date, "%Y-%m-%d").date()
        print("##############Just after Expiration###############")
        product.location = location
        print("##############Just Before Save###############")
        product.save()
        print("##############Just After Save###############")
        querySet = Product.objects.all()
        temp = []
        object_list = []
        for i in range(len(querySet)):
            querySet[i].days_remaining = (parser.parse(str(querySet[i].expiration_date)) - datetime.now()).days
            temp.append(querySet[i])
            if (i + 1) % 3 == 0:
                object_list.append(temp)
                temp = []
        if len(temp) != 0:
            object_list.append(temp)
        context = {"object_list": object_list}
        return render(request, 'myPantry.html', context)


class MyMeal(View):
    def get(self, request, *args, **kwargs):
        querySet = Meal.objects.all()
        context = {"object_list" : querySet}
        return render(request, 'myMeal.html', context)


class MyOrders(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'myOrders.html')
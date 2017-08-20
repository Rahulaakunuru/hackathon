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
        food_expiry_date = request.GET['food_expiration_date'].strip()
        food_id = Product.objects.all().count() + 1
        location = 'Fridge'
        product = Product()
        product.food_id = str(food_id)
        product.food_name = food_name
        print(type(food_expiry_date))
        product.expiration_date = parser.parse(food_expiry_date)
        product.location = location
        product.save()
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
        return render(request, 'myMeal.html')


class MyOrders(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'myOrders.html')
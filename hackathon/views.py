from django.views.generic import View
from django.shortcuts import render
from datetime import datetime
from dateutil import parser

from .models import Product


class MyPantry(View):
    def get(self, request, *args, **kwargs):
        search_string = request.GET['search_string']
        print(search_string)
        if(search_string is None or search_string. == ""):
            querySet = Product.objects.all()
        else:
            querySet = Product.objects.filter(food_name__contains=search_string)
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
        #print(context)
        return render(request, 'myPantry.html', context)


class MyMeal(View):
    def get(self, request, *args, **kwargs):
        querySet = Product.objects.all()
        context = {"object_list" : querySet}
        return render(request, 'myMeal.html', context)


class MyOrders(View):
    def get(self, request, *args, **kwargs):
        querySet = Product.objects.all()
        context = {"object_list" : querySet}
        return render(request, 'myOrders.html', context)
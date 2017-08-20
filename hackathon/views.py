from django.views.generic import View
from django.shortcuts import render

from .models import Product

class MyPantry(View):
    def get(self, request, *args, **kwargs):
        querySet = Product.objects.all()
        context = {"object_list" : querySet}
        return render(request, 'myPantry.html', context)
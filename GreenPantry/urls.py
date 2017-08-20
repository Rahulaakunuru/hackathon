"""GreenPantry URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

from hackathon.views import MyPantry
from hackathon.views import MyMeal
from hackathon.views import MyOrders
from hackathon.views import MyPantrySearch

urlpatterns = [
    url(r'^admin/', admin.site.urls),
url(r'^myPantry/', MyPantry.as_view()),
url(r'^myMeal/', MyMeal.as_view()),
url(r'^myOrders/', MyOrders.as_view()),
url(r'^searchPantry/', MyPantrySearch.as_view()),
]

from django.shortcuts import render
from .models import news, Category

# Create your views here.
def home(request):
    dict = {
          'name' : news.objects.all(),
          'price': 999,
          'address' : 'Chabahil'
        }

    return render(request, "index.html", dict)


def about(request):
    return render(request,'about.html')
from django.shortcuts import render
from .models import news, Category

# Create your views here.
def home(request):
    dict = {
          'name' : news.objects.all(),
          'price': 999,
          'address' : 'Chicago'
        }

    return render(request, "index.html", dict)


def about(request):
    return render(request,'about.html')


def newsDetails(request, id):
    print(id)
    data = news.objects.get(id = id)
    return render(request, "newsDetails.html", {'data':data})
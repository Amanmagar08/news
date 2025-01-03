from django.shortcuts import render

# Create your views here.
def home(request):
    dict = {
          'name' : 'item',
          'price': '$999'
        }

    return render(request, "index.html", dict)


def about(request):
    return render(request,'about.html')
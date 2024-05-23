from urllib import request

#from django.http import HttpResponse
from django.shortcuts import render
from . models import Place, Professor

# Create your vie


def demo(request):
    #name = "India"
    obj = Place.objects.all()
    obj1 = Professor.objects.all()
    return render(request, 'index.html', {'result': obj, 'results': obj1})


#def about(request):
 #   return render(request, 'about.html')


#def contact(request):
 #   return HttpResponse("hello am contact")


#def operations(request):
    #x = int(request.GET['num1'])
    #y = int(request.GET['num2'])
    #res = x + y
    #res1 = x - y
    #res2 = x * y
    #res3 = x // y
    #return render(request, 'result.html', {'result': {res,res1,res2,res3}})



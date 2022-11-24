from django.shortcuts import render,HttpResponse

# Create your views here.
def index(request):
    return render(request,'index.html')

def generate():
  from random import randrange
  num = randrange(100000,1000000)
  return num

def output(request):
    context = {
        'number': generate()
    }
    return render(request,'index.html',context)
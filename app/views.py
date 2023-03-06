from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def gagan(request):
    return HttpResponse('<h1>My name is Gagan sir!!</h1>')
def naveen(request):
    return HttpResponse('<marquee><h1>Navven tinnava era vadilestum</h1></marquee>')
def raju(request):
    return HttpResponse('<h3>what the ____(dash) do you want?</h3>')
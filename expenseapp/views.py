from django.shortcuts import render
from django.views.decorators.csrf import ensure_csrf_cookie,csrf_exempt
from django.http import HttpResponse
# Create your views here.



def helloWorld(request):
    return render(request,'index.html')
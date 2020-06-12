from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')
def count(request):
    return render(request, 'count.html')
def msg(request):
    return render(request, 'msg.html')
def flow(request):
    return render(request, 'flow.html')


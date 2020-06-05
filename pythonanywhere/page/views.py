from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# Create your views here.
def page(request):
    return render(request, 'output2.html')

def second(request):
    return render(request, 'output1.html')


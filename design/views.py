from django.shortcuts import render

# Create your views here.

def productsresponsive(request):
    context = {}
    return render(request, 'design/productsresponsive.html', context)
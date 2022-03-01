from django.shortcuts import render
from ecart.models import Product
from django.db.models import Q

# Create your views here.
def SeachResult(request):
    products=None
    query=None
    if 'q' in request.GET:
        query=request.GET.get('q')
        products=Product.objects.all().filter(Q(name__contains=query) | Q(describtion__contains=query))
    return render(request,'search.html',{'query':query,'products':products})
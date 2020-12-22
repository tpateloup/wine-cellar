from django.shortcuts import render

from .models import Bottle

# Main page
def index(request):
    return render(request, 'wine_cellars/index.html')

# List of bottles
def bottles(request):
    bottles = Bottle.objects.order_by('year')
    context = { 'bottles': bottles }
    return render(request, 'wine_cellars/bottles.html', context)

# Display one bottle
def bottle(request, bottle_id):
    bottle = Bottle.objects.get(id=bottle_id)
    context = { 'bottle': bottle }
    return render(request, 'wine_cellars/bottle.html', context)

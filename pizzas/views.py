from django.shortcuts import render
from .models import Pizza,Topping

# Create your views here.
def index(request):
    """The home page for Learning Log"""
    return render(request, 'pizzas/index.html')

def pizzas(request):
   
    pizza = Pizza.objects.order_by('date_added')
    context = {'pizza': pizza}
    return render(request, 'pizzas/pizza.html', context)

def toppings(request,idv):
    

    topping = Topping.objects.filter(pizza_id=idv)
    context = {'topping': topping}
    return render(request, 'pizzas/toppings.html', context)

from django.shortcuts import render, redirect

from pizzas.models import Comments, Pizza, Topping, Comments
from pizzas.forms import CommentsForm


# Create your views here.
def index(request):
    return render(request, 'pizzas/index.html')

def pizza_type(request,pizza_id):       #2 types of requests in HTML, get and post. "Get" views the database and pulls info                                     #"Post" adds new info into the database
    pizza = Pizza.objects.get(id= pizza_id)
    toppings = pizza.topping_set.all()
    context = {'toppings':toppings}
    
    return render(request, 'pizzas/pizza_type.html', context)


def pizza_menu(request):        #2 types of requests in HTML, get and post. "Get" views the database and pulls info
    pizzas = Pizza.objects.filter().order_by()                                        #"Post" adds new info into the database

    context = {'pizzas':pizzas}
    
    return render(request, 'pizzas/pizza_menu.html', context)



def new_comment(request):

    if request.method != 'POST':
        form = CommentsForm()

    else:
        form = CommentsForm(data=request.POST)

        if form.is_valid():
            new_comment = form.save()
            return redirect('pizzas:pizza_menu')

    context = {'form':form}
    return render(request, 'pizzas/new_comment.html', context)

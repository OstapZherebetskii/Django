from django.shortcuts import render, redirect
import requests
from .models import Order
from .forms import OrderForm
from django.views.generic import DetailView, DeleteView

# Create your views here.
def index(request):
    return render(request, 'main/main.html', {'name': 'Home page'} )

class OrderDetailView(DetailView):
    model = Order
    template_name = 'main/order_detail.html'
    context_object_name = 'order'

class OrderDeleteView(DeleteView):
    model = Order
    success_url = '/orders/'
    template_name = 'main/order_delete.html'
    
    

def about(request):
    res = requests.get('https://jsonplaceholder.typicode.com/posts')
    text = res.json()
    
    return render(request, 'main/hello_there.html', {'text':text})

def orders(request):
    orders = Order.objects.order_by("-date")
    return render(request, 'main/orders.html', {'orders': orders})


def new_order(request):
    error = ''
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('orders')
        else:
            error = 'Error'
    form = OrderForm()
    data = {
        'form': form,
        'error': error
    }
    return render(request, 'main/new_order.html', data)
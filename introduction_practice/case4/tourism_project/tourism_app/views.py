from django.shortcuts import render, redirect, get_object_or_404
from .models import Tour, Service, Client, Operator, Order
from .forms import TourForm, ServiceForm, ClientForm, OperatorForm, OrderForm

def home(request):
    return render(request, 'tourism_app/home.html')

# Tours
def tour_list(request):
    tours = Tour.objects.all()
    return render(request, 'tourism_app/tour_list.html', {'tours': tours})

def add_tour(request):
    if request.method == 'POST':
        form = TourForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tour_list')
    else:
        form = TourForm()
    return render(request, 'tourism_app/add_tour.html', {'form': form})

# Services
def service_list(request):
    services = Service.objects.all()
    return render(request, 'tourism_app/service_list.html', {'services': services})

def add_service(request):
    if request.method == 'POST':
        form = ServiceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('service_list')
    else:
        form = ServiceForm()
    return render(request, 'tourism_app/add_service.html', {'form': form})

# Clients
def client_list(request):
    clients = Client.objects.all()
    return render(request, 'tourism_app/client_list.html', {'clients': clients})

def add_client(request):
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('client_list')
    else:
        form = ClientForm()
    return render(request, 'tourism_app/add_client.html', {'form': form})

# Operators
def operator_list(request):
    operators = Operator.objects.all()
    return render(request, 'tourism_app/operator_list.html', {'operators': operators})

def add_operator(request):
    if request.method == 'POST':
        form = OperatorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('operator_list')
    else:
        form = OperatorForm()
    return render(request, 'tourism_app/add_operator.html', {'form': form})

# Orders
def order_list(request):
    orders = Order.objects.all()
    return render(request, 'tourism_app/order_list.html', {'orders': orders})

def add_order(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('order_list')
    else:
        form = OrderForm()
    return render(request, 'tourism_app/add_order.html', {'form': form})

def confirm_delete(request, item_type, item_id):
    item = None
    if item_type == 'tour':
        item = get_object_or_404(Tour, pk=item_id)
        item_name = item.tour_name
    elif item_type == 'service':
        item = get_object_or_404(Service, pk=item_id)
        item_name = item.service_name
    elif item_type == 'client':
        item = get_object_or_404(Client, pk=item_id)
        item_name = f"{item.first_name} {item.last_name}"
    elif item_type == 'operator':
        item = get_object_or_404(Operator, pk=item_id)
        item_name = item.operator_name
    elif item_type == 'order':
        item = get_object_or_404(Order, pk=item_id)
        # Assume Orders might need more complex handling; adjust as needed
        item_name = f"Order #{item_id}"
    else:
        return redirect('home')  # Handle unknown type

    if request.method == 'POST':
        item.delete()
        return redirect(f'{item_type}_list')  # Redirect to the list page of the item type

    return render(request, 'tourism_app/confirm_delete.html', {
        'item_name': item_name,
        'item_type': item_type.capitalize(),  # Capitalize item type for display
    })
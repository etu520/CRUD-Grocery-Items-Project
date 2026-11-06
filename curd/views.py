from django.shortcuts import render, redirect, get_object_or_404
from .models import GroceryItem

# List all items
def grocery_list(request):
    items = GroceryItem.objects.all()
    return render(request, 'grocery_list.html', {'items': items})

# Create a new item
def grocery_create(request):
    if request.method == 'POST':
        name = request.POST['name']
        quantity = request.POST['quantity']
        price = request.POST['price']
        GroceryItem.objects.create(name=name, quantity=quantity, price=price)
        return redirect('grocery_list')
    return render(request, 'grocery_form.html')

# Update an existing item
def grocery_update(request, pk):
    item = get_object_or_404(GroceryItem, pk=pk)
    if request.method == 'POST':
        item.name = request.POST['name']
        item.quantity = request.POST['quantity']
        item.price = request.POST['price']
        item.save()
        return redirect('grocery_list')
    return render(request, 'grocery_form.html', {'item': item})

# Delete an item
def grocery_delete(request, pk):
    item = get_object_or_404(GroceryItem, pk=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('grocery_list')
    return render(request, 'grocery_confirm_delete.html', {'item': item})


# Create your views here.
from django.shortcuts import render, redirect
from .models import List
from .forms import ListForm
from django.contrib import messages


def home(request):
     if request.method == 'POST':
         form = ListForm(request.POST or None)


         if form.is_valid():
             form.save()
             all_items = List.objects.all()
             messages.success(request, ('Item has been added to list!'))
             return render(request, 'taskmanagement/home.html', {'all items': all_items})

     else:
        all_items = List.objects.all()
        return render(request, 'taskmanagement/home.html', {'all items': all_items})

def delete(request,List_id):
    item = List.objects.get(pk=List_id)
    item.delete()
    messages.success(request,('Item HAs Been Deleted!'))
    return redirect('home')

def cross_off(request, List_id):
    item = List.objects.get(pk=List_id)
    item.completed = True
    item.save()
    return redirect('home')
def uncross(request, List_id):
    item = List.objects.get(pk=List_id)
    item.completed = False
    item.save()
    return redirect('home')

def edit(request, List_id):
    if request.method == 'POST':
        item = List.objects.get(pk=List_id)
        form = ListForm(request.POST or None, instance=item)

        if form.is_valid():
            form.save()
            messages.success(request,('Item Has been Edited!'))
            return redirect('home')
    else:
        item = List.objects.get(pk=List_id)
        return render(request, 'taskmanagement/edit.html', {'item': item})
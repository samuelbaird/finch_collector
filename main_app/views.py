from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Finch, Sighting, Food
from .forms import SightingForm

finches = [
  {'name': 'Lolo', 'breed': 'tabby', 'description': 'furry little demon', 'age': 3},
  {'name': 'Sachi', 'breed': 'calico', 'description': 'gentle and loving', 'age': 2},
]

# Create your views here.

def home (request):
    return render(request, 'home.html')

def about (request):
    return render(request, 'about.html')

def finches_index (request):
    finches = Finch.objects.all()
    return render(request, 'finches/index.html', {
        'finches': finches
    })

def finches_detail (request, finch_id):
    finch = Finch.objects.get(id=finch_id)
    id_list = finch.food.all().values_list('id')
    food_finch_doesnt_eat = Food.objects.exclude(id__in = id_list)
    sighting_form = SightingForm()
    return render(request, 'finches/detail.html', {
        'finch': finch, 'sighting_form': sighting_form,
        'food' : food_finch_doesnt_eat
    })

class FinchCreate(CreateView):
    model = Finch
    fields = ['common_name', 'scientific_name', 'beak_type',]

class FinchUpdate(UpdateView):
    model = Finch
    fields = ['common_name', 'scientific_name', 'beak_type',]

class FinchDelete(DeleteView):
    model = Finch
    success_url = '/finches/'

def add_sighting(request, finch_id):
    form = SightingForm(request.POST)
    if form.is_valid():
        new_sighting = form.save(commit=False)
        new_sighting.finch_id = finch_id
        new_sighting.save()
    return redirect('detail', finch_id=finch_id)

def assoc_food(request, finch_id, food_id):
    Finch.objects.get(id=finch_id).food.add(food_id)
    return redirect('detail', finch_id=finch_id)

def unassoc_food(request, finch_id, food_id):
    Finch.objects.get(id=finch_id).food.remove(food_id)
    return redirect('detail', finch_id=finch_id)
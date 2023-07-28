from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Finch
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
    sighting_form = SightingForm()
    return render(request, 'finches/detail.html', {
        'finch': finch, 'sighting_form': sighting_form
    })

class FinchCreate(CreateView):
    model = Finch
    fields = '__all__'

class FinchUpdate(UpdateView):
    model = Finch
    fields = ['common_name', 'scientific_name', 'beak_type', 'food']

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
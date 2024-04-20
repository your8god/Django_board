from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from .models import Bb, Rublic

def index(request):
    items = Bb.objects.all()
    rublics = Rublic.objects.all()
    return render(request, 'myapp/index.html', {'bb':items, 'rublics': rublics})

def index_page(request, board_id):
    res = get_object_or_404(Bb, pk=board_id)
    return render(request, 'myapp/index_page.html', {'item':res, 'rublics': Rublic.objects.all()})

def rublic_page(request, rublic_id):
    cur_rublic = get_object_or_404(Rublic, pk=rublic_id)
    items = Bb.objects.filter(rublic=cur_rublic)
    rublics = Rublic.objects.all()
    return render(request, 'myapp/rublic_page.html', {'c_rublic':cur_rublic, 'items':items, 'rublics':rublics})
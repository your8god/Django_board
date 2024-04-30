from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.db import models
from django.core.paginator import Paginator

from .models import Bb, Rublic
from .forms import BbForm


def index(request):
    items = Bb.objects.all()
    rublics = Rublic.objects.all()
    paginator = Paginator(items, 3)
    number = request.GET.get('page', 1)
    page = paginator.get_page(number)
    return render(request, 'myapp/index.html', {'items':page, 'rublics': rublics})


def index_page(request, board_id):
    res = get_object_or_404(Bb, pk=board_id)
    return render(request, 'myapp/index_page.html', {'item':res, 'rublics': Rublic.objects.all()})


def rublic_page(request, rublic_id):
    cur_rublic = get_object_or_404(Rublic, pk=rublic_id)
    items = Bb.objects.filter(rublic=cur_rublic)
    rublics = Rublic.objects.all()
    paginator = Paginator(items, 3)
    page = paginator.page(request.GET.get('page', 1))
    return render(request, 'myapp/rublic_page.html', {'c_rublic':cur_rublic, 'items':page, 'rublics':rublics})


class BbCreateView(CreateView):
    template_name = 'myapp/create.html'
    form_class = BbForm
    success_url = reverse_lazy('myapp:main')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['rublics'] = Rublic.objects.all()
        for k, v in context.items():
            print(f'key {k}:\nvalue: {v}')
        return context 
    

class BbUpdateView(UpdateView):
    form_class = BbForm
    template_name = 'myapp/update.html'
    success_url = reverse_lazy('myapp:main')
    model = Bb

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['rublics'] = Rublic.objects.all()
        return context 
    
    def get(self, request, *args, **kwargs) -> HttpResponse:
        print(self)
        print(request)
        print(kwargs)
        return super().get(request, *args, **kwargs)
    

class BbDeleteView(DeleteView):
    model = Bb
    #form_kwargs = {'rublic_id':}
    #success_url = 'bboard/rublic/{rublic_id}'
    success_url = reverse_lazy('myapp:rublic_page', kwargs={'rublic_id': '{rublic_id}'})
    template_name = 'myapp/delete.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['rublics'] = Rublic.objects.all()
        print(context)
        return context 
    
    def post(self, request, *args, **kwargs):
        print(self, request, kwargs, args, sep='\n')
        return super().post(request, *args, **kwargs)
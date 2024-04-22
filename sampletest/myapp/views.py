from django.shortcuts import render, get_object_or_404
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

from .models import Bb, Rublic
from .forms import BbForm


def index(request):
    items = Bb.objects.all()
    rublics = Rublic.objects.all()
    return render(request, 'myapp/index.html', {'items':items, 'rublics': rublics})


def index_page(request, board_id):
    res = get_object_or_404(Bb, pk=board_id)
    return render(request, 'myapp/index_page.html', {'item':res, 'rublics': Rublic.objects.all()})


def rublic_page(request, rublic_id):
    cur_rublic = get_object_or_404(Rublic, pk=rublic_id)
    items = Bb.objects.filter(rublic=cur_rublic)
    rublics = Rublic.objects.all()
    return render(request, 'myapp/rublic_page.html', {'c_rublic':cur_rublic, 'items':items, 'rublics':rublics})


class BbCreateView(CreateView):
    template_name = 'myapp/create.html'
    form_class = BbForm
    success_url = reverse_lazy('myapp:main')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['rublics'] = Rublic.objects.all()
        return context 
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic import ListView
from django.urls import reverse

from myapp.models import Bike

class BikeDetailView(DetailView):
    model = Bike
    template_name = 'bike_detail.html'
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['home_url'] = reverse('home')
        return context

class BikeCreateView(CreateView):
    model = Bike
    template_name = 'bike_create.html'
    fields = ['type','price','image']

class BikeUpdateView(UpdateView):
    model = Bike
    template_name = 'bike_create.html'
    fields = ['type','price','image']

class BikeListView(ListView):
    model = Bike
    paginate_by = 3
    #queryset=Bike.objects.filter(type='mountain')
    template_name = 'bike_list.html'
from django.views.generic.detail import DetailView
from myapp.models import Bike

class BikeDetailView(DetailView):
    model = Bike
    template_name = 'bike_detail.html'
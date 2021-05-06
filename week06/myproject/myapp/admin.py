from django.contrib import admin
from myapp.models import Bike

class BikeAdmin(admin.ModelAdmin):
    list_display=['id','start','type','price']

admin.site.register(Bike, BikeAdmin)
"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from myapp.views import BikeDetailView, BikeCreateView, BikeUpdateView, BikeListView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('bike/<int:pk>', BikeDetailView.as_view(),name='bike'),
    path('bike_create/', BikeCreateView.as_view(),name='bike_create'),
    path('bike_update/<int:pk>', BikeUpdateView.as_view(),name='bike_update'),
    path('bikes/', BikeListView.as_view(),name='bikes'),
    path('', BikeListView.as_view(),name='home'),
]

from django.conf import settings
from django.conf.urls.static import static
urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
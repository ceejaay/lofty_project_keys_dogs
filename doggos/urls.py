from django.urls import path
from . import views

app_name = 'doggos'
urlpatterns = [
        path('', views.DogViewSet.as_view({'get': 'get_dog'}), name="dogs"),

        ]

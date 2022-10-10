from django.urls import path
from . import views

app_name = 'keys'
urlpatterns = [
        path('', views.KeyViewSet.as_view({'get': 'keys', 'post': 'keys'}), name="keys"),

        path('key_detail/<int:pk>/', views.KeyViewSet.as_view({'get': 'key_detail', 'put': 'key_detail'}), name="key"),

        ]

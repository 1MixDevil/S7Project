from django.urls import path
from .views import index, GetData

urlpatterns = [
    path('add/', GetData.as_view(), name='add'),
    path('', index, name='index')
]
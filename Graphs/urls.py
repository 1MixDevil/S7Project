from django.urls import path
from .views import index, GetData, finish

urlpatterns = [
    path('add/', GetData.as_view(), name='add'),
    path('', index, name='index'),
    path('finish/', finish, name='finish')
]
from django.urls import path
from .views import *

urlpatterns = [
    path('', uploadview, name='uplaod' )
]

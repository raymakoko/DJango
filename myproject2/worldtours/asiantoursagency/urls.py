from django.urls import path
from . import views

# Define a list of Url patterns
urlpatterns = [
    path('',views.index)
    
]
from django.urls import path
from . import views

# Define list of Url patterns
urlpatterns = [
    path('',views.index)
]
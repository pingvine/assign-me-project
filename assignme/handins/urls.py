from django.urls import path
from . import views

urlpatterns = [
    path("", views.handins_index, name="handins_index"),
]

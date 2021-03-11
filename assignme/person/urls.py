from django.urls import include, path
from . import views

urlpatterns = [
    path("", views.person_index, name="person_index"),
    path("<int:pk>/",
         views.person_detail,
         name="person_detail"),
]

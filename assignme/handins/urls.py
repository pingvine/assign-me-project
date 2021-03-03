from django.urls import path
from . import views

urlpatterns = [
    path("", views.handins_index, name="handins_index"),
    path("<int:pk>/", views.handin_detail, name="handin_detail"),
    path("new/", views.new_handin, name="new_handin"),
]

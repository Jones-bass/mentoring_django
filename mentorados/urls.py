from django.urls import path
from . import views

urlpatterns = [
    path("mentorados/", views.mentorados, name="mentorados"),
]

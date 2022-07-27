
from django.urls import path
from . import views

urlpatterns = [
    path("",views.hello),
    path("message/",views.message),
    path("app/",views.app)
]
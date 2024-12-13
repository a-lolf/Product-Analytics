from django.urls import path
from .views import *

urlpatterns = [
    path("products/analytics/", ProductsViewset.as_view()),
]
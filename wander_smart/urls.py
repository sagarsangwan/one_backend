from django.urls import path
from .views import GenerateTripPlan

urlpatterns = [
    path("generate-trip-plan/", GenerateTripPlan.as_view(), name="generate-trip-plan"),
]

from django.urls import path
from .views import RevenueStatisticView

urlpatterns = [
    path('revenues/', RevenueStatisticView.as_view()),
]

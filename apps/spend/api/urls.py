from django.urls import path
from .views import SpendStatisticView

urlpatterns = [
    path('spends/', SpendStatisticView.as_view()),
]

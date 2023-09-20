from django.db.models import Sum
from rest_framework import generics

from .serializers import RevenueStatisticSerializer
from ..models import RevenueStatistic


class RevenueStatisticView(generics.ListAPIView):
    serializer_class = RevenueStatisticSerializer

    def get_queryset(self):
        queryset = RevenueStatistic.objects.select_related('spend').values('date', 'name').annotate(
            total_revenue=Sum('revenue'),
            total_spend=Sum('spend__spend'),
            total_impressions=Sum('spend__impressions'),
            total_clicks=Sum('spend__clicks'),
            total_conversion=Sum('spend__conversion')
        )
        return queryset

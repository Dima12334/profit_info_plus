from django.db.models import Sum
from rest_framework.generics import ListAPIView

from .serializers import SpendStatisticSerializer
from ..models import SpendStatistic


class SpendStatisticView(ListAPIView):
    serializer_class = SpendStatisticSerializer

    def get_queryset(self):
        queryset = SpendStatistic.objects.prefetch_related('revenuestatistic_set').values('date', 'name').annotate(
            total_spend=Sum('spend'),
            total_impressions=Sum('impressions'),
            total_clicks=Sum('clicks'),
            total_conversion=Sum('conversion'),
            total_revenue=Sum('revenuestatistic__revenue')
        )
        return queryset

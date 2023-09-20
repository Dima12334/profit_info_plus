from rest_framework import serializers

from apps.spend.models import SpendStatistic


class SpendStatisticSerializer(serializers.ModelSerializer):
    total_spend = serializers.DecimalField(max_digits=10, decimal_places=2)
    total_impressions = serializers.IntegerField()
    total_clicks = serializers.IntegerField()
    total_conversion = serializers.IntegerField()
    total_revenue = serializers.IntegerField()

    class Meta:
        model = SpendStatistic
        fields = (
            "name",
            "date",
            "total_spend",
            "total_impressions",
            "total_clicks",
            "total_conversion",
            "total_revenue",
        )

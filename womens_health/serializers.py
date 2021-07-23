from rest_framework import serializers
from rest_framework.response import Response
from .models import WomenCycle, GeneratedCycle

class WomenCycleSerializers(serializers.ModelSerializer):
    last_period_date = serializers.DateField()
    cycle_average = serializers.IntegerField()
    Period_average = serializers.IntegerField()
    start_date = serializers.DateField()
    end_date = serializers.DateField()

    class Meta:
        model = WomenCycle
        fields = ['id','last_period_date','cycle_average','Period_average','start_date', 'end_date',]

    def create(self, validated_data):
        return WomenCycle.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.last_period_date = validated_data.get('last_period_date', instance.last_period_date)
        instance.cycle_average = validated_data.get('cycle_average', instance.cycle_average)
        instance.Period_average = validated_data.get('Period_average', instance.Period_average)
        instance.Period_average = validated_data.get('Period_average', instance.Period_average)
        instance.save()
        return instance


class GetEventsDateSerializers(serializers.ModelSerializer):
    event = serializers.CharField()
    date = serializers.DateField()

    class Meta:
        model = GeneratedCycle
        fields = ['event','date']
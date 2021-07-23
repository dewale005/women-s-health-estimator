from datetime import datetime

from django.shortcuts import render
from rest_framework import generics

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter

from rest_framework.response import Response

from .models import WomenCycle, GeneratedCycle

from utilities.Calculator import GenerateCycle

from .serializers import WomenCycleSerializers, GetEventsDateSerializers

class Create_cycles(generics.CreateAPIView):
    queryset = WomenCycle.objects.all()
    serializer_class = WomenCycleSerializers

    def post(self, request, *arg, **kwarg):
        last_period_date = datetime.strptime(request.data.get('last_period_date'), "%Y-%m-%d")
        cycle_average = request.data.get('cycle_average')
        Period_average = request.data.get('Period_average')
        start_date = datetime.strptime(request.data.get('start_date'), "%Y-%m-%d")
        end_date = datetime.strptime(request.data.get('end_date'), "%Y-%m-%d")
        cycle_list = GenerateCycle(
            last_period_date=last_period_date, 
            cycle_average=int(cycle_average), 
            Start_date=start_date, 
            end_date=end_date, 
            period_average=int(Period_average)
            )
        serializer = WomenCycleSerializers(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        GeneratedCycle.objects.bulk_create([GeneratedCycle(**each) for each in cycle_list['data']])
        return Response({"total_created_cycles": cycle_list['total_created_cycles'] }, status=200)


class Update_cycle(generics.RetrieveUpdateAPIView):
    queryset = WomenCycle.objects.all()
    serializer_class = WomenCycleSerializers

    def update(self, request, *arg, **kwarg):
        last_period_date = datetime.strptime(request.data.get('last_period_date'), "%Y-%m-%d")
        cycle_average = request.data.get('cycle_average')
        Period_average = request.data.get('Period_average')
        start_date = datetime.strptime(request.data.get('start_date'), "%Y-%m-%d")
        end_date = datetime.strptime(request.data.get('end_date'), "%Y-%m-%d")
        cycle_list = GenerateCycle(
            last_period_date=last_period_date, 
            cycle_average=int(cycle_average), 
            Start_date=start_date, 
            end_date=end_date, 
            period_average=int(Period_average)
            )
        serializer = WomenCycleSerializers(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=200)


class GetEventDate(generics.ListAPIView):
    queryset = GeneratedCycle.objects.all()
    serializer_class = GetEventsDateSerializers
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['date']
    search_fields = ['date']
    ordering_fields = ['date', 'id']
    ordering = ['id']
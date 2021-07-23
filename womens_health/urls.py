from django.urls import path, include

from .views import Create_cycles, Update_cycle, GetEventDate

urlpatterns = [
    path('create-cycles', Create_cycles.as_view(), name="women_cycle"),
    path('create-cycles/<int:pk>', Update_cycle.as_view(), name="women_cycle_datail"),
    path('cycles-events', GetEventDate.as_view(), name="women_cycle_datail"),
]
from rest_framework import viewsets, filters, generics
from apps.staff.api.serializers import (
    StaffSerializer, PositionSerializer, ScheduleStaffSerializer, ScheduleStaffUpdateSerializer
)
from apps.staff.models import Staff, Position, ScheduleStaff
import django_filters.rest_framework as django_filter
from rest_framework.response import Response


class StaffView(viewsets.ModelViewSet):
    serializer_class = StaffSerializer
    queryset = Staff.objects.all()
    filter_backends = [django_filter.DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    ordering_fields = "__all__"
    
    
class PositionView(viewsets.ModelViewSet):
    serializer_class = PositionSerializer
    queryset = Position.objects.all()
    filter_backends = [django_filter.DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    ordering_fields = "__all__"
    
    
class ScheduleStaffView(viewsets.ModelViewSet):
    serializer_class = ScheduleStaffSerializer
    queryset = ScheduleStaff.objects.all()
    filter_backends = [django_filter.DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    ordering_fields = "__all__"
    
    
class ScheduleStaffUpdateView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ScheduleStaffUpdateSerializer
    queryset = ScheduleStaff.objects.all()
    
    def delete(self, request, *args, **kwargs):
        try:
            return self.destroy(request, *args, **kwargs)
        except Exception as e:
            return Response({"message": f"The schedule staff does not exist."}, status=500)

from rest_framework import viewsets
from RestApp.models import Booking
from RestApp.serializers import BookingSerializer

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    http_method_names = ['get', 'post', 'patch', 'delete']
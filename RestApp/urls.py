from django.urls import path, include
from rest_framework.routers import DefaultRouter
from RestApp.views import MovieViewSet, BookingViewSet


router = DefaultRouter()
router.register(r'movies', MovieViewSet, basename='movie')
router.register(r'bookings', BookingViewSet, basename='booking')

urlpatterns = [
    path('', include(router.urls)),
]
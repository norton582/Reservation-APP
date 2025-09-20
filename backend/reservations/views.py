
from rest_framework import viewsets, permissions
from .models import *
from .serializers import *


# Create your views here.
class ChambreViewSet(viewsets.ModelViewSet):
    queryset = Chambre.objects.all()
    serializer_class = ChambreSerializer

class ReservationViewSet(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        #Associer automatiquement la reservation à l'utilisateur connecté
        serializer.save(user=self.request.user)
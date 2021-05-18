from rest_framework import permissions
from rest_framework.viewsets import ModelViewSet
from .models import UserFC
from .serializers import GetUserFCSerializer, GetUserFCPublicSerializer


class UserFCPublicVIew(ModelViewSet):
    queryset = UserFC.objects.all()
    serializer_class = GetUserFCPublicSerializer
    permission_classes = [permissions.AllowAny]


class UserFCView(ModelViewSet):
    serializer_class = GetUserFCSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return UserFC.objects.filter(id = self.request.user.id)


from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from rest_framework.decorators import action
from rest_framework.response import Response

from core.users.models import User
from core.users.serializers import UserSerializer

class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_permissions(self):
        # Se for o método create (POST), permite qualquer pessoa
        if self.action == 'create':
            return [AllowAny()]
        # Se for 'me', permite apenas autenticados
        elif self.action == 'me':
            return [IsAuthenticated()]
        # Outras ações: aplique o padrão
        return [IsAuthenticated()]
    
    @action(detail=False, methods=["get"], permission_classes=[IsAuthenticated])
    def me(self, request):
        serializer = self.get_serializer(request.user)
        return Response(serializer.data)

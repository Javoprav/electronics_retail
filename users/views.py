from rest_framework import generics
from users.models import UserRoles, User
from users.serializers.serializers import ForCreateUserSerializers, ForAuthUserSerializers


class UsersListView(generics.ListAPIView):
    """Контроллер для списка пользователей"""
    serializer_class = ForAuthUserSerializers
    queryset = User.objects.all()


class UsersDetailView(generics.RetrieveAPIView):
    """Контроллер для деталей пользователя"""
    serializer_class = ForAuthUserSerializers
    queryset = User.objects.all()

    def get_queryset(self):
        """Показывает детали пользователя с проверкой на владельца или модератора, или супеюзера"""
        user = self.request.user
        if user.is_staff or user.is_superuser or user.role == UserRoles.MODERATOR:
            return User.objects.all()
        else:
            return User.objects.filter(pk=user.id)


class UsersCreateView(generics.CreateAPIView):
    """Контроллер для создания пользователя"""
    serializer_class = ForCreateUserSerializers
    queryset = User.objects.all()


class UsersUpdateView(generics.UpdateAPIView):
    """Контроллер для обновления пользователя"""
    serializer_class = ForCreateUserSerializers
    queryset = User.objects.all()

    def get_queryset(self):
        """Обновление пользователя доступно только самому пользователю или модератору, или суперюзеру"""
        user = self.request.user
        if user.is_staff or user.is_superuser or user.role == UserRoles.MODERATOR:
            return User.objects.all()
        else:
            return User.objects.filter(pk=user.id)

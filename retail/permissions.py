from rest_framework.permissions import BasePermission


class IsActive(BasePermission):
    """Проверка пользователя на активность"""
    message = 'Вы являетесь активным!'

    def has_permission(self, request, view):
        if not request.user.is_active:
            return False
        return True

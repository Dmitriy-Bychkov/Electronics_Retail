from rest_framework.permissions import BasePermission


class IsActiveUser(BasePermission):
    """
    Настройка прав, чтобы только активные
    пользователи имели доступ к API
    """

    def has_object_permission(self, request, view, obj):
        if request.user.is_active:
            return True

        return False

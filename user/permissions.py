from rest_framework.permissions import BasePermission

class UserIsEmployeePermission(BasePermission):
    def has_permission(self, request, view):
        user = request.user
        return user.is_authenticated and hasattr(user, 'employee')
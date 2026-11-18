from rest_framework import permissions

class CustomUserPermission(permissions.BasePermission):
    message = "permission denied. booking is unreachable"

    def has_permission(self, request, view):
        user = request.user
        group = user.groups.first()

        if user.is_superuser:
            return True
        for permission  in group.permissions.all():
            if permission.codename == "view_booking":
                return True
        return False

from rest_framework import permissions


class UpdateProfile(permissions.BasePermission):
    """Allows users to upadate their own profiles"""

    def has_object_permission(self, request, view, obj):
        """Check if user can modify their own profile"""

        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.id == request.user.id


class UpdateStore(permissions.BasePermission):
    """Allows users to upadate their own items"""

    def has_object_permission(self, request, view, obj):
        """Check if user can modify their own item"""

        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.id == request.user.id

from rest_framework.permissions import BasePermission

class IsUserAsOwner(BasePermission):
    """
    Ensures that the client is modifying its own properties
    """

    def has_object_permission(self, request, view, obj):
        return obj == request.user

from django.contrib.auth.models import AnonymousUser
from rest_framework import permissions


from users.models import UserRoles


class AdUpdateDeletePermission(permissions.IsAuthenticatedOrReadOnly):
    message = 'Update and Delete ads only for authors and admins.'

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        if isinstance(request.user, AnonymousUser):
            return False
        if request.user.role == UserRoles.ADMIN:
            return True
        if request.user == obj.author:
            return True
        return False

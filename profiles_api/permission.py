from rest_framework import permissions

class UpdateOwnprofie(permissions.BasePermission):
    """ Allow user to their own profile"""

    def has_object_permission(self, request, veiw, obj):
        """check user is trying to edit their own profile"""
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.id == request.user.id

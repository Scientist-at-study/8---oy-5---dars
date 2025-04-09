from rest_framework import permissions



class IsAdminCreateReadDeleteOnly(permissions.BasePermission):
    """
    Admin ozgartirishdan tashqari hamma ruhsat bor
    product larni srogini ozgartralmasligi uchun qilingan
    """

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True

        if request.method == 'POST':
            return request.user and request.user.is_staff

        if request.method == 'DELETE':
            return request.user and request.user.is_staff

        return False


class IsClientReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.method in permissions.SAFE_METHODS


class IsClientCreateReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True

        if request.method == 'POST':
            return request.user and request.user.is_authenticated

        return False

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return obj.client == request.user.client
        return False

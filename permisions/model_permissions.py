from rest_framework.permissions import DjangoModelPermissions as ModelPermission, BasePermission


class DjangoModelPermission(ModelPermission):
    pass


class IsOwnerPermission(BasePermission):

    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated)

    def has_object_permission(self, request, view, obj):
        return obj.owner == request.user

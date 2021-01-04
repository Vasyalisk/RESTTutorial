from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    '''
    Custom permission to only allow owners of an object to edit it.
    '''
    
    def has_object_permission(self, request, view, obj):
        # Safe methods (GET, HEAD, OPTIONS) are allowed for read at any time
        if request.method  in permissions.SAFE_METHODS:
            return True
        # Write access only to owner of the snippet
        else:
            return obj.owner == request.user
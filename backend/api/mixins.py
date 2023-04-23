from .permissions import IsStaffEditiorPermission
from rest_framework import permissions


class StaffEditorPermissionMixin():
    permission_classes = [permissions.IsAdminUser,IsStaffEditiorPermission]
from .permissions import IsStaffEditiorPermission
from rest_framework import permissions


class StaffEditorPermissionMixin():
    permission_classes = [permissions.IsAdminUser, IsStaffEditiorPermission]


class UserQuerySetMixin():
    user_field = 'user'
    allow_staff_view = False

    def get_queryset(self, *args, **kwargs):
        lookup_data = {}

        user = self.request.user  # type: ignore
        lookup_data[self.user_field] = user  # type: ignore
        print(lookup_data)
        qs = super().get_queryset(*args, **kwargs)  # type: ignore
        print(qs)
        if self.allow_staff_view and user.is_staff:  # type: ignore
            return qs
        return qs.filter(**lookup_data)

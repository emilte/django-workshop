from guardian import models as guardian_models

from django.contrib import admin
from django.contrib.auth.models import Permission, Group
from django.contrib.admin.models import LogEntry
from django.contrib.sessions.models import Session
from django.contrib.contenttypes.models import ContentType

from blog.custom_classes.admin_classes import (
    CustomGuardedUserAdmin,
    CustomGuardedGroupAdmin,
    CustomGuardedModelAdmin,
)

from .models import (
    User,
    FieldDisplay,
)

# Common fields:
# ordering = []
# sortable_by = []
# list_filter = []
# list_display = ['id', '__str__']
# search_fields = []
# filter_horizontal = []
# list_display_links = ['id', '__str__']
# autocomplete_fields = []
# list_select_related = True

### Django models ###

# Unregister User and Group to set new Admins.
admin.site.unregister(Group)


@admin.register(User)
class UserAdmin(CustomGuardedUserAdmin):
    sortable_by = [
        'id', 'username', 'email', 'first_name', 'last_name', 'is_active', 'is_staff', 'is_superuser', 'last_login',
        'date_joined'
    ]
    list_display = [
        'id', 'username', 'email', 'first_name', 'last_name', 'is_active', 'is_staff', 'is_superuser',
        'group_memberships', 'last_login', 'date_joined'
    ]
    list_display_links = ['id', 'username']
    list_select_related = True

    @admin.display(empty_value='all')
    def group_memberships(self, obj: User) -> int:
        n: int = obj.groups.all().count()
        return n


@admin.register(Group)
class GroupAdmin(CustomGuardedGroupAdmin):
    sortable_by = ['id', 'name']
    list_display = ['id', 'name', 'members']
    list_display_links = ['id', 'name']
    list_select_related = True

    def members(self, obj: Group) -> int:
        n: int = obj.user_set.all().count()
        return n


@admin.register(Permission)
class PermissionAdmin(CustomGuardedModelAdmin):
    # ordering = []
    sortable_by = ['id', 'codename', 'content_type']
    # list_filter = []
    list_display = ['id', '__str__', 'codename', 'content_type']
    search_fields = ['name', 'codename', 'content_type__app_label', 'content_type__model']
    # filter_horizontal = []
    list_display_links = ['id', '__str__']
    autocomplete_fields = ['content_type']
    list_select_related = True


@admin.register(ContentType)
class ContentTypeAdmin(CustomGuardedModelAdmin):
    # ordering = []
    # sortable_by = []
    list_filter = ['id', 'app_label', 'model']
    list_display = ['id', '__str__', 'app_label', 'model']
    search_fields = ['app_label', 'model']
    # filter_horizontal = []
    list_display_links = ['id', '__str__']
    # autocomplete_fields = []
    list_select_related = True


@admin.register(LogEntry)
class LogEntryAdmin(CustomGuardedModelAdmin):
    sortable_by = ['id', 'user', 'action_flag', 'object_repr', 'action_time']
    list_filter = ['action_flag']
    list_display = ['id', '__str__', 'user', 'action_flag', 'object_repr', 'action_time']
    _user_search_fields = UserAdmin.custom_search_fields(prefix='user')
    search_fields = ['id', 'object_repr', *_user_search_fields]
    # filter_horizontal = []
    list_display_links = ['id', '__str__']
    autocomplete_fields = ['user', 'content_type']
    list_select_related = True


@admin.register(Session)
class SessionAdmin(CustomGuardedModelAdmin):
    # ordering = []
    sortable_by = ['session_key', 'expire_date']
    # list_filter = []
    list_display = ['session_key', 'expire_date']
    search_fields = ['session_key', 'session_data']
    # filter_horizontal = []
    list_display_links = ['session_key']
    # autocomplete_fields = []
    list_select_related = True


### End: Django models ###


### Guardian models ###
@admin.register(guardian_models.GroupObjectPermission)
class GroupObjectPermissionAdmin(CustomGuardedModelAdmin):
    list_display = ['id', '__str__', 'permission', 'group', 'content_type']
    list_display_links = ['id', '__str__']


@admin.register(guardian_models.UserObjectPermission)
class UserObjectPermissionAdmin(CustomGuardedModelAdmin):
    ordering = ['user']
    sortable_by = ['id', 'user', 'permission', 'content_type']
    # list_filter = [] # TODO
    _user_search_fields = UserAdmin.custom_search_fields(prefix='user')
    list_display = ['id', '__str__', 'user', 'permission', 'content_type']
    search_fields = [*_user_search_fields]
    # filter_horizontal = [] # TODO
    list_display_links = ['id', '__str__']
    autocomplete_fields = ['user', 'permission', 'content_type']
    list_select_related = True


### End: Guardian models ###

### Our models ###


@admin.register(FieldDisplay)
class FieldDisplayAdmin(CustomGuardedModelAdmin):
    # ordering = ['user']
    # sortable_by = ['id', 'user', 'permission', 'content_type']
    list_display = [
        'id', '__str__', 'charfield', 'charfield_unique', 'unique_together_one', 'unique_together_two',
        'charfield_unique', 'textfield', 'boolean', 'time', 'date', 'boolean', 'choices', 'foreignkey', 'duration',
        'file_field', 'email', 'float_field', 'integer', 'email', 'image', 'json', 'url', 'uuid', 'updated', 'created'
    ]
    list_filter = ['choices']
    search_fields = ['id']
    filter_horizontal = ['many_to_many']
    autocomplete_fields = ['foreignkey']
    # list_select_related = True

    readonly_fields = ['updated', 'created']


### End: Our models ###

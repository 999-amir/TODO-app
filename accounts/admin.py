from django.contrib import admin
from .models import CostumeUser
from django.contrib.auth.models import Group
from .forms import CostumeUserCreationForm, CostumeUserChangeForm
from django.contrib.auth.admin import UserAdmin


class CostumeUserAdmin(UserAdmin):
    form = CostumeUserChangeForm
    add_form = CostumeUserCreationForm

    list_display = ('email', 'is_admin', 'last_login')
    list_filter = ('is_admin',)
    fieldsets = (
        (
            'USER-INFORMATION',
            {'fields': ('email', 'password')}
        ),
        (
            'USER-PERMISSIONS',
            {'fields': ('is_active', 'is_admin')}
        ),
        (
            'DATE',
            {'fields': ('last_login', 'updated', 'created')}
        )
    )
    add_fieldsets = (
        (
            'CREATE-USER',
            {'fields': ('email', 'password_1', 'password_2')}
        ),
    )
    search_fields = ('email',)
    ordering = ('email', 'last_login', 'created')
    filter_horizontal = ()
    readonly_fields = ('last_login', 'updated', 'created')


admin.site.unregister(Group)
admin.site.register(CostumeUser, CostumeUserAdmin)

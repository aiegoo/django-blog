from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Ouser


@admin.register(Ouser)
class OuserAdmin(UserAdmin):
    list_display = ('username', 'email', 'is_staff', 'is_active', 'date_joined')
    fieldsets = (
        ('basic information', {'fields': (('username', 'email', 'password'), ('link',))}),
        ('Authority information', {'fields': (('is_active', 'is_staff', 'is_superuser'),
                             'groups', 'user_permissions')}),
        ('Important date', {'fields': (('last_login', 'date_joined'),)}),
    )
    filter_horizontal = ('groups', 'user_permissions',)
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups')
    search_fields = ('username', 'email')

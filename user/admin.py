from django.contrib import admin

from user.models import User


@admin.register(User)
class ClientUserAdmin(admin.ModelAdmin):
    '''user management config'''
    list_display = ['username', 'email', 'phoneNumber', 'date_joined', 'is_active', 'first_name',
                    'last_name']
    list_filter = ['username', 'is_active', 'phoneNumber']
    list_editable = ['is_active']

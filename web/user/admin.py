from django.contrib import admin
from .models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_per_page = 30
    list_display = ('username', 'email',
                    'is_staff', 'is_active', 'date_joined')
    list_filter = ('date_joined', )
    search_fields = ('username', )



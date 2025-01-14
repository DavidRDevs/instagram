from django.contrib import admin
from .models import UserProfiles, Follow

# Register your models here.


@admin.register(UserProfiles)
class UserProfileAdmin(admin.ModelAdmin):

    list_display = ('user', 'birth_date', 'created_at')
    import_order = ('id',)
    export_order = ('id',)


@admin.register(Follow)
class FollowAdmin(admin.ModelAdmin):

    list_display = ('follower', 'following', 'created_at')
    import_order = ('id',)
    export_order = ('id',)

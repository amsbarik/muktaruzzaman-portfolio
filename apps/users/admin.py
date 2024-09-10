from django.contrib import admin
from .models import Team, Role, Gender, UserSetting

# Register your models here.
class GenderAdmin(admin.ModelAdmin):
    list_display = ('name',)
admin.site.register(Gender, GenderAdmin)

class RoleAdmin(admin.ModelAdmin):
    list_display = ('name',)
admin.site.register(Role, RoleAdmin)

class TeamAdmin(admin.ModelAdmin):
    list_display = ('member_id', 'name', 'profile_img', 'mobile', 'email', 'nid', 'passport', 'gender', 'address', 'nationality', 'religion', 'birth_date', 'blood', 'join_date', 'rejoin_date', 'role', 'skill',)
    
admin.site.register(Team, TeamAdmin)





admin.site.register(UserSetting) 
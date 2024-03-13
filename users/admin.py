from django.contrib import admin

from .models import *

# Register your models here.
class CourseAdmin(admin.ModelAdmin):
    list_display = ("name", "date_created", "date_modified")
    
class IMUserAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "is_active", "user_type")

class CohortAdmin(admin.ModelAdmin):
    list_display = ("name", "description", "year", "start_date", "end_date", "is_active", "date_created", "date_modified", "author")

class CohortMemberAdmin(admin.ModelAdmin):
    list_display = ("cohort", "member", "is_active", "date_created", "date_modified", "author")


# Register each model with its corresponding custom admin configuration
admin.site.register(IMUser, IMUserAdmin)
admin.site.register(Cohort, CohortAdmin)
admin.site.register(CohortMember, CohortMemberAdmin)


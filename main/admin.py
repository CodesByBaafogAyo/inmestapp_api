from django.contrib import admin
from .models import *

# Register your models here.
class CourseAdmin(admin.ModelAdmin):
    list_display = ("name", "date_created", "date_modified")
    
    
class CohortMemberAdmin(admin.ModelAdmin):
    list_display = ("cohort", "member", "is_active", "date_created", "date_modified", "author")

class ClassScheduleAdmin(admin.ModelAdmin):
    list_display = ("title", "start_date_and_time", "end_date_and_time", "is_repeated", "is_active", "cohort", "venue")

class ClassAttendanceAdmin(admin.ModelAdmin):
    list_display = ("class_schedule", "attendee", "is_present", "date_created", "date_modified", "author")

class QueryAdmin(admin.ModelAdmin):
    list_display = ("title", "submitted_by", "assigned_to", "resolution_status", "date_created", "date_modified", "author")

class QueryCommentAdmin(admin.ModelAdmin):
    list_display = ("query", "comment", "date_created", "date_modified", "author")

# Register each model with its corresponding custom admin configuration
admin.site.register(Course, CourseAdmin)
admin.site.register(ClassSchedule, ClassScheduleAdmin)
admin.site.register(ClassAttendance, ClassAttendanceAdmin)
admin.site.register(Query, QueryAdmin)
admin.site.register(QueryComment, QueryCommentAdmin)

from typing import Any
from django.db import models
import datetime

from users.models import Cohort, IMUser

# Create your models here.

class Course(models.Model):
    name = models.CharField(max_length = 1000, blank=True, null = True)
    description = models.TextField(default='N/A', blank=True, null = True)
    date_created = models.DateTimeField(auto_now_add = True, blank=True, null = True)
    date_modified = models.DateTimeField(auto_now=True, blank=True, null = True)

class ClassSchedule(models.Model):
    title = models.CharField(max_length = 64, blank=True, null = True)
    description = models.TextField(default='N/A', blank=True, null = True)
    start_date_and_time = models.DateTimeField(blank=True, null = True)
    end_date_and_time = models.DateTimeField(blank=True, null = True)
    is_repeated = models.BooleanField(default = True)
    repeat_frequency = models.IntegerField(default = 3)
    is_active = models.BooleanField(default = True)
    # organizer = models.CharField(max_length = 64, blank=True, null = True)
    organizer = models.ForeignKey(IMUser, on_delete=models.CASCADE, max_length = 64, blank=True, null = True, related_name = "classschedule_organizer")
    cohort = models.ForeignKey(Cohort, on_delete=models.CASCADE, related_name = "classschedule_cohort")
    venue = models.CharField(default = "GL", max_length = 64, blank=True, null = True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name = "classschedule_course" )
    
class ClassAttendance(models.Model):
    class_schedule = models.ForeignKey(ClassSchedule, on_delete=models.CASCADE, related_name = "classattendance_class_schedule")
    attendee = models.ForeignKey(IMUser, on_delete=models.CASCADE, related_name = "classattendance_attendee")
    is_present = models.BooleanField(default = False)
    date_created = models.DateTimeField(auto_now_add = True, blank=True, null = True)
    date_modified = models.DateTimeField(auto_now=True, blank=True, null = True)
    author = models.ForeignKey(IMUser, on_delete=models.CASCADE, related_name = "classattendance_author" )
    
    
class Query(models.Model):
    class ResolutionStatus(models.TextChoices):
        PENDING = "PENDING",
        IN_PROGRESS = "IN_PROGRESS",
        DECLINED = "DECLINED",
        RESOLVED = "RESOLVED"
        
    title = models.CharField(default = "", max_length = 64, blank=True, null = True)
    description = models.TextField(default='N/A', blank=True, null = True)
    submitted_by = models.ForeignKey(IMUser, on_delete=models.CASCADE, related_name = "query_submitted_by" )
    assigned_to = models.ForeignKey(IMUser, on_delete=models.CASCADE, related_name = "query_assigned_to" )
    resultion_status = models.CharField(choices = ResolutionStatus.choices, default = ResolutionStatus.PENDING, max_length = 20)
    date_created = models.DateTimeField(auto_now_add = True, blank=True, null = True)
    date_modified = models.DateTimeField(auto_now=True, blank=True, null = True)
    author = models.ForeignKey(IMUser, on_delete=models.CASCADE, related_name = "query_author" )
    
    
class QueryComment(models.Model):
    query =  models.ForeignKey(Query, on_delete=models.CASCADE, related_name = "querycomment_query" )
    comment = models.CharField(default = "", max_length = 64, blank=True, null = True)
    date_created = models.DateTimeField(auto_now_add = True, blank=True, null = True)
    date_modified = models.DateTimeField(auto_now=True, blank=True, null = True)
    author = models.ForeignKey(IMUser, on_delete=models.CASCADE, related_name = "querycomment_author" )
   
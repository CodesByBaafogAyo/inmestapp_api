from django.db import models

# Create your models here.
class IMUser(models.Model):
    class UserType(models.TextChoices):
        EIT = "EIT",
        TEACHING_FELLOW = "TEACHING_FELLOW",
        ADMIN_STAFF = "ADMIN_STAFF",
        ADMIN = "ADMIN"
        
    first_name = models.CharField(max_length = 64, blank=True, null = True)
    last_name = models.CharField(max_length = 64, blank=True, null = True)
    is_active = models.BooleanField(default = True)
    user_type = models.CharField(choices = UserType.choices, default = UserType.EIT, max_length = 20)
    date_created = models.DateTimeField(auto_now_add = True, blank=True, null = True)
    date_modified = models.DateTimeField(auto_now=True, blank=True, null = True)
    email = models.EmailField(max_length = 64)
    
class Cohort(models.Model):
    name = models.CharField(max_length = 64, blank=True, null = True)
    description = models.TextField(default='N/A', blank=True, null = True)
    year = models.IntegerField(default = 1920)
    start_date = models.DateTimeField(blank=True, null = True)
    end_date = models.DateTimeField(blank=True, null = True)
    is_active = models.BooleanField(default = True)
    date_created = models.DateTimeField(auto_now_add = True, blank=True, null = True)
    date_modified = models.DateTimeField(auto_now=True, blank=True, null = True)
    author = models.ForeignKey(IMUser, on_delete=models.CASCADE, related_name = "cohort_author" )
    
    
class CohortMember(models.Model):
    cohort = models.ForeignKey(Cohort, on_delete=models.CASCADE, related_name = "cohortmember_cohort")
    member = models.ForeignKey(IMUser, on_delete=models.CASCADE, related_name = "cohortmember_member")
    is_active = models.BooleanField(default = True)
    date_created = models.DateTimeField(auto_now_add = True, blank=True, null = True)
    date_modified = models.DateTimeField(auto_now=True, blank=True, null = True)
    author = models.ForeignKey(IMUser, on_delete=models.CASCADE, related_name = "cohormember_author" )


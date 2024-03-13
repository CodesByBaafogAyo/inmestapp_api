from datetime import timezone
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.dispatch import receiver
from django.db.models.signals import post_save
from rest_framework.authtoken.models import Token
from django.utils import timezone

class IMUser(AbstractUser):
    USER_TYPES = (
        ('EIT', 'EIT'),
        ('TEACHING_FELLOW', 'TEACHING FELLOW'),
        ('ADMIN_STAFF', 'ADMINISTRATIVE STAFF'),
        ('ADMIN', 'ADMINSTRATOR'),
    )
    first_name = models.CharField(max_length=155, blank=True, default="")
    last_name = models.CharField(max_length=155, blank=True, default="")
    middle_name = models.CharField(max_length=155, blank=True, default="")
    phone_number = models.CharField(max_length=20, blank=True, default="")
    unique_code = models.CharField(max_length=20, blank=True)
    temporal_login_fails = models.IntegerField(default=0)
    permanent_login_fails = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)
    is_blocked = models.BooleanField(default=False)
    user_type = models.CharField(max_length=20, choices=USER_TYPES, null=True)
    date_modified = models.DateTimeField(default=timezone.now)
    date_created = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"

@receiver(post_save, sender=IMUser)
def generate_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        token = Token.objects.create(user=instance)
        token.save()

# Set a default value for the 'password' field
IMUser._meta.get_field('password').default = timezone.now


class Cohort(models.Model):
    name = models.CharField(max_length=255, default = "")
    description = models.TextField(blank=True, default = "")
    year = models.IntegerField()
    start_date = models.DateField()
    end_date = models.DateField()
    is_active = models.BooleanField(default=True)
    date_created = models.DateTimeField(default=timezone.now)
    date_modified = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(IMUser, related_name="cohort_author", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} ({self.year})"
    
class CohortMember(models.Model):
    cohort = models.ForeignKey(Cohort, on_delete=models.CASCADE, related_name='cohort')
    member = models.ForeignKey(IMUser, on_delete=models.CASCADE, related_name='cohort_member')
    is_active = models.BooleanField(default=True)
    date_created = models.DateTimeField(default=timezone.now)
    date_modified = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(IMUser, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.member.first_name} {self.member.last_name} ({self.cohort.name})"
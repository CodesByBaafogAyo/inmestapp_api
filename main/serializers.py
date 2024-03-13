from rest_framework import serializers
from users.serializers import *
from users.models import *
from main.models import *


class CourseModelSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'name', 'description')
        model = Course
        
class CourseSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    description = serializers.CharField()
    date_created = serializers.DateField()


class ClassScheduleSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField()
    description = serializers.CharField() 
    start_date_and_time = serializers.DateTimeField()
    end_date_and_time = serializers.DateTimeField()
    is_repeated = serializers.BooleanField()
    repeat_frequency = serializers
    organizer = UserSerializer(many = False)
    cohort = CohortSerializer(many = False)
    venue = serializers.CharField() 
    course = CourseSerializer()
    meeting_type = serializers.CharField()
    facilitator = UserSerializer(many = False)
    date_created = serializers.DateField()
  

class ClassAttendanceSerializer(serializers.Serializer):
    class_schedule = ClassScheduleSerializer()
    attendee = UserSerializer(many = False)
    author = UserSerializer(many = False)

class QuerySerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=200)
    description = serializers.CharField()
    author = UserSerializer(many = False)
    submitted_by = UserSerializer(many = False)
    assigned_to = UserSerializer(many = False)


class QueryCommentSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    query = QuerySerializer()
    comment = serializers.CharField()
    author = UserSerializer(many = False)
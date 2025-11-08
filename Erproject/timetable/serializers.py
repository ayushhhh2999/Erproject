from rest_framework import serializers
from .models import TimeTable, Subject, Classroom

class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = '__all__'


class ClassroomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classroom
        fields = '__all__'


class TimeTableSerializer(serializers.ModelSerializer):
    faculty_name = serializers.CharField(source='faculty.username', read_only=True)
    subject_name = serializers.CharField(source='subject.name', read_only=True)
    classroom_name = serializers.CharField(source='classroom.name', read_only=True)

    class Meta:
        model = TimeTable
        fields = [
            'id', 'faculty', 'faculty_name', 'subject', 'subject_name',
            'classroom', 'classroom_name', 'day_of_week', 'start_time', 'end_time'
        ]

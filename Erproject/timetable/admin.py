from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Subject, Classroom, TimeTable

@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ("name", "code")

@admin.register(Classroom)
class ClassroomAdmin(admin.ModelAdmin):
    list_display = ("name",)

@admin.register(TimeTable)
class TimeTableAdmin(admin.ModelAdmin):
    list_display = ("faculty", "day_of_week", "start_time", "end_time", "subject", "classroom")
    list_filter = ("day_of_week", "faculty", "classroom")
    search_fields = ("faculty__username", "subject__name", "classroom__name")

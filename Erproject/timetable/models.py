from django.db import models

class Subject(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return f"{self.name} ({self.code})"


class Classroom(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class TimeTable(models.Model):
    DAYS = [
        ("MONDAY", "Monday"),
        ("TUESDAY", "Tuesday"),
        ("WEDNESDAY", "Wednesday"),
        ("THURSDAY", "Thursday"),
        ("FRIDAY", "Friday"),
        ("SATURDAY", "Saturday"),
        ("SUNDAY", "Sunday"),
    ]

    # ✅ Use string reference instead of importing or calling get_user_model()
    faculty = models.ForeignKey(
        "home.User", on_delete=models.CASCADE, related_name="timetables"
    )
    classroom = models.ForeignKey("timetable.Classroom", on_delete=models.CASCADE, related_name="timetables")
    subject = models.ForeignKey("timetable.Subject", on_delete=models.CASCADE, related_name="timetables")
    day_of_week = models.CharField(max_length=10, choices=DAYS)
    start_time = models.TimeField()
    end_time = models.TimeField()

    class Meta:
        unique_together = ("faculty", "day_of_week", "start_time", "end_time")
        ordering = ["day_of_week", "start_time"]

    def __str__(self):
        return (
            f"{self.faculty.username} - {self.day_of_week} "
            f"({self.start_time.strftime('%H:%M')}–{self.end_time.strftime('%H:%M')}) "
            f"| {self.subject.name}"
        )

from rest_framework import viewsets, permissions
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import TimeTable
from .serializers import TimeTableSerializer


class IsAdminOrReadOnly(permissions.BasePermission):
    """Allow only admins/superusers to modify timetable."""
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user.is_staff or request.user.is_superuser


class TimeTableViewSet(viewsets.ModelViewSet):
    queryset = TimeTable.objects.all()
    serializer_class = TimeTableSerializer
    permission_classes = [IsAdminOrReadOnly]

    def get_queryset(self):
        user = self.request.user

        # Faculty — see their own timetable
        if user.role == "FACULTY":
            return TimeTable.objects.filter(faculty=user)

        # Student — see timetable of their classroom
        elif user.role == "STUDENT":
            personal_detail = getattr(user, "personal_detail", None)
            if personal_detail and personal_detail.classroom:
                return TimeTable.objects.filter(classroom=personal_detail.classroom)
            return TimeTable.objects.none()

        # Admin / staff — see all
        elif user.is_superuser or user.is_staff:
            return TimeTable.objects.all()

        return TimeTable.objects.none()

    # Get timetable by faculty username
    @action(detail=False, methods=["get"], url_path="faculty/(?P<faculty_name>[^/.]+)")
    def by_faculty(self, request, faculty_name=None):
        timetables = TimeTable.objects.filter(faculty__username=faculty_name)
        return Response(TimeTableSerializer(timetables, many=True).data)

    # Get timetable by classroom name
    @action(detail=False, methods=["get"], url_path="class/(?P<classroom_name>[^/.]+)")
    def by_class(self, request, classroom_name=None):
        timetables = TimeTable.objects.filter(classroom__name=classroom_name)
        return Response(TimeTableSerializer(timetables, many=True).data)


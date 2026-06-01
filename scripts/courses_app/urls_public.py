"""
Public URL routing for courses_app
Mounted at /api/ via oj/urls.py
"""
from django.conf.urls import url
from .views import (
    CourseListAPI,
    CourseDetailAPI,
)

urlpatterns = [
    url(r"^courses/?$", CourseListAPI.as_view(), name="course_list"),
    url(r"^course/detail/?$", CourseDetailAPI.as_view(), name="course_detail"),
]

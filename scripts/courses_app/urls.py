"""
Admin URL routing for courses_app
Mounted at /api/admin/ via oj/urls.py
"""
from django.conf.urls import url
from .views import (
    CourseAdminAPI,
    ChapterAdminAPI,
    ProblemAssignmentAdminAPI,
    MoveProblemAdminAPI,
    SyncCourseContestAPI,
    ProblemTitlesAPI,
)

urlpatterns = [
    url(r"^groups/courses/?$", CourseAdminAPI.as_view(), name="admin_courses"),
    url(r"^groups/chapters/?$", ChapterAdminAPI.as_view(), name="admin_chapters"),
    url(r"^groups/problems/?$", ProblemAssignmentAdminAPI.as_view(), name="admin_course_problems"),
    url(r"^groups/problems/move/?$", MoveProblemAdminAPI.as_view(), name="admin_course_problem_move"),
    url(r"^groups/sync_contest/?$", SyncCourseContestAPI.as_view(), name="admin_course_sync_contest"),
    url(r"^groups/problem_titles/?$", ProblemTitlesAPI.as_view(), name="admin_problem_titles"),
]

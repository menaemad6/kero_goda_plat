import core.views
from django.urls import path

from . import views





# Views 

urlpatterns = [
    path('lessons', views.lessons, name='lessons'),
    path('lessons/' , views.grades , name="lecture-grades"),

    path('lessons/<slug:slug>' , views.lecture_detail , name="lesson-detail"),
    path('lessons/progress/<slug:slug>' , views.lecture_progress , name="lesson-progress"),

    path('chapters/<slug:slug>' , views.chapter_detail , name="chapter-detail"),
    path('chapters/progress/<slug:slug>' , views.chapter_progress , name="chapter-progress"),


    path('groups' , views.groups , name="groups"),
    path('groups/<slug:slug>' , views.group_detail , name="group-page"),


    path('teachers', views.teachers, name='teachers'),
    path('teachers/<slug:slug>', views.teacher_lectures, name='teacher-lectures'),


    path('get-premium', core.views.get_premium, name='premium-page'),
    path('purchased-lessons', views.purchased_lessons, name='purchased-lessons'),
]








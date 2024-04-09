import core.views
from . import views
from django.urls import path

import activity.views



#Views
urlpatterns = [
    # Teacher URLS
    path('dashboard/assignments' , views.dashboard_assignments , name="assignments"),
    path('dashboard/assignment/<slug:slug>' , views.dashboard_assignment_detail , name="assignment"),
    path('dashboard/assignment/applicants/<slug:slug>' , views.assignment_applicants , name="assignment-detail"),
    path('dashboard/assignment/answers/<slug:slug>' , views.dashboard_student_answers , name="student-answers"),


    # Student URLS
    path('assignment/<slug:slug>' , views.assignment_detail , name="assignment-detail-page"),
    path('assignment/progress/<slug:slug>' , views.assignment_progress , name="assignment-progress-page"),
]






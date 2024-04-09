import core.views
from . import views
from django.urls import path

import activity.views






#Functions
urlpatterns = [
    path('dashboard/create-lecture' , views.create_lecture , name="create-lecture"),
    path('dashboard/add-video' , views.add_video, name="add-video"),
    path('dashboard/add-part' , views.add_part, name="add-part"),
    path('dashboard/delete-part' , views.delete_part, name="delete-part"),

    path('dashboard/group-settings' , views.group_settings , name="group-settings"),
    path('dashboard/delete-group' , views.delete_group , name="group-delete"),


    path('dashboard/create-chapter' , views.create_chapter , name="create-chapter"),
    path('dashboard/delete-chapter' , views.delete_chapter , name="delete-chapter"),
    path('dashboard/chapter-settings' , views.chapter_settings, name="chapter-settings"),

    path('delete-lesson', views.delete_lesson, name='dashboard-delete-lesson'),
    path('delete-code', views.delete_code, name='dashboard-delete-code'),
    path('delete-assignment', views.delete_assignment, name='dashboard-delete-assignment'),
    path('dashboard-delete-assignment', views.dashboard_delete_assignment, name='dashboard-delete-assignment'),

    path('upload', views.upload, name='upload'),
    path('code-generator', views.code_generator, name='code-generator'),
    path('dashboard-edit-student', views.dashboard_profiles, name='dashboard-edit-student'),

    path('wallet/code-charge', views.code_charge_function, name='wallet-code-recharge-function'),


    path('chapter-code-charge', views.chapter_code_charge, name='chapter-code-recharge'),
    path('lesson-code-charge', views.lesson_code_charge, name='code-recharge'),
    path('code-charge-function', views.code_charge_function, name='code-recharge-function'),
]


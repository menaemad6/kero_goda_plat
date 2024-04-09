import core.views
from . import views
from django.urls import path

import activity.views






#Functions
urlpatterns = [
    # Teacher URLS
    path('dashboard/create-assignment' , views.create_assignment  , name="create-assignment"),
    path('dashboard/add-question' , views.add_question, name="add-question"),
    path('dashboard/edit-question' , views.edit_question, name="edit-question"),
    path('dashboard/delete-question' , views.delete_question, name="delete-question"),



    # Student URLS
    path('assignment-start' , views.assignment_start, name="assignment-start"),
    path('save-answer' , views.assignment_save_answer, name="assignment-save-answer"),
    path('submit-assignment' , views.assignment_submit, name="assignment-submit"),
]



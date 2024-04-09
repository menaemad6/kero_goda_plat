from django.urls import path
from . import views

# Views 
urlpatterns = [
    path('', views.index, name='main'),
    path('profile/<str:pk>', views.profile, name='profile'),
    path('settings', views.settings, name='settings'),
    path('settings-teacher', views.settings_teacher, name='settings-teacher'),
    path('setup-account/1', views.setup_acount_step1, name='setup-account-step1'),
    path('setup-account/2', views.setup_acount_step2, name='setup-account-step2'),

    path('setup-account-social/1', views.allauth_setup_acount_step1, name='setup-account-social-step1'),
    path('setup-account-social/2', views.allauth_setup_acount_step2, name='setup-account-social-step2'),

    path('setup-account/creating-profile', views.creating_profile ,  name='setup'),
    path('setup', views.allauth_setup_acount, name='setup'),
    path('setup/creating-profile', views.creating_profile ,  name='setup'),
    path('setup-account-teacher', views.setup_acount_teacher, name='setup-account-teacher'),



    path('inbox', views.inbox, name='inbox'),
    path('notifications', views.notifications, name='inbox'),
    
    path('logins', views.account_logins, name='inbox'),


    path('news', views.news, name='news-page'),
    path('news/<slug:slug>' , views.news_detail , name="new-page"),


    path('signup', views.signup, name='signup'),
    path('register', views.register, name='register'),
    path('login', views.login, name='signin'),
]



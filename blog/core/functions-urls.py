from django.urls import path
from . import views




# Functions 
urlpatterns = [
    path('follow', views.follow, name='follow'),


    path('like-post', views.like_post, name='like-post'),
    path('like-lesson', views.like_lesson, name='like-lesson'),
    path('like-dashboard', views.like_dashboard, name='like-dashboard'),

    path('buy-lesson', views.purchase_lesson, name='buy-lesson'),
    path('buy-chapter', views.purchase_chapter, name='buy-chapter'),

    path('comment', views.comment, name='comment'),
    path('reply', views.reply, name='reply'),
    path('delete-reply', views.delete_reply, name='delete-reply'),
    path('delete-comment', views.delete_comment, name='delete-reply'),

    path('delete-notification', views.delete_notification, name='delete-notification'),

    path('login-function', views.login_function, name='login-function'),
    path('signup-function', views.signup_function, name='signup-function'),
    path('logout', views.logout, name='logout'),

    path('reset-platform', views.reset_platform, name='reset-notifications'),

    path('search', views.search, name='search'),
    path('search-page', views.search_page, name='search-page'),

]





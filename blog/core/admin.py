from django.contrib import admin
from .models import Profile, Post, LikePost, FollowersCount , Instructor , News , GetPremium , Subject , BuyLesson
from .models import RechargeRequest , Code , Comment , Reply , Activity , Notification , Part , Info , Chapter , ChapterLecture , BuyChapter
from .models import Group , GroupMember , GroupLecture



class MainAdmin(admin.ModelAdmin):
    list_display =  ['user' ,'phone' , 'year' , 'premium' , 'instructor' , 'admin' , 'public', 'money' , 'no_of_buys']
    list_editable = ['year' , 'premium' , 'instructor' , 'admin' ,'public', 'money' , 'no_of_buys']



admin.site.register(Profile , MainAdmin)
admin.site.register(Post)
admin.site.register(Part)
admin.site.register(Chapter)
admin.site.register(ChapterLecture)
admin.site.register(Group)
admin.site.register(GroupMember)
admin.site.register(GroupLecture)
admin.site.register(Comment)
admin.site.register(Reply)
# admin.site.register(RechargeRequest)
admin.site.register(Code)
admin.site.register(BuyLesson)
admin.site.register(BuyChapter)
admin.site.register(Activity)
admin.site.register(Notification)
# admin.site.register(GetPremium)
# admin.site.register(Subject)
# admin.site.register(News)
admin.site.register(Instructor)
admin.site.register(LikePost)
admin.site.register(FollowersCount)
admin.site.register(Info)
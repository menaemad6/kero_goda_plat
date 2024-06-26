from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from .models import AssignmentSubmit
from .models import Notification , Assignment , Activity , Reply , Comment, Code , RechargeRequest, Profile, Post, Part, LikePost, FollowersCount , Subject , GetPremium , News , Instructor , BuyLesson , Info , Chapter , ChapterLecture , BuyChapter , Question , Answer  , Info , AssignmentSubmit , AssignmentOpen
from .models import Group , GroupLecture , GroupMember 
from itertools import chain
import random



from django.shortcuts import get_object_or_404
# Create your views here.


def error_404(request , exception):
    return render(request , 'error-404.html' , status=404)


def reset_platform(request):
    if User.objects.filter(username=request.user.username).first():
        user_object = User.objects.get(username=request.user.username)
        user_profile = Profile.objects.get(user=user_object)

        notifications_count = Notification.objects.filter(username=request.user.username).count()
    else:
        user_profile = ''
        notifications_count = ''

    if user_profile.instructor == True:
        delete_lectures = Post.objects.all().delete()
        delete_lectures_parts = Part.objects.all().delete()
        delete_lectures_purchases = BuyLesson.objects.all().delete()
        delete_chapter_purchases = BuyChapter.objects.all().delete()
        delete_chapters = Chapter.objects.all().delete()
        delete_chapters_lectures = ChapterLecture.objects.all().delete()
        delete_groups = Group.objects.all().delete()
        delete_group_members = GroupMember.objects.all().delete()
        delete_group_lectures = GroupLecture.objects.all().delete()
        delete_activities = Activity.objects.all().delete()
        delete_all_notifications = Notification.objects.all().delete()
        delete_replys = Reply.objects.all().delete()
        delete_comments = Comment.objects.all().delete()
        delete_codes = Code.objects.all().delete()
        delete_likes = LikePost.objects.all().delete()
        delete_assignments = Assignment.objects.all().delete()
        delete_assignment_questions = Question.objects.all().delete()
        delete_assignment_answers = Answer.objects.all().delete()
        delete_assignment_open = AssignmentOpen.objects.all().delete()
        delete_assignment_submit = AssignmentSubmit.objects.all().delete()
        delete_logins = Info.objects.all().delete()





        return redirect('/')
    else:
        return redirect('/')











def index(request):
    if User.objects.filter(username=request.user.username).first():
        user_object = User.objects.get(username=request.user.username)
        user_profile = Profile.objects.get(user=user_object)

        notifications_count = Notification.objects.filter(username=request.user.username).count()
    else:
        user_profile = ''
        notifications_count = ''



    instructor = Profile.objects.filter(instructor=True)
    subject = Subject.objects.all()


    lessons_list = [1,]
    lessons_feed = []

    bought_lists = Post.objects.all()
    lessons_feed.append(bought_lists)
    purchased_lessons_list = list(chain(*lessons_feed))

    lectures = Post.objects.filter(type='normal').order_by('-created_at')




    return render(request, 'main/index.html', {'instructor':instructor , 'lectures':lectures   , 'user_profile': user_profile , 'subject':subject , 'notifications' : notifications_count})

@login_required(login_url='register')
def news(request):
    if User.objects.filter(username=request.user.username).first():
        user_object = User.objects.get(username=request.user.username)
        user_profile = Profile.objects.get(user=user_object)

        notifications_count = Notification.objects.filter(username=request.user.username).count()
    else:
        user_profile = ''
        notifications_count = ''

    news = News.objects.all()
    context = {'news' : news , 'user_profile': user_profile , 'notifications' : notifications_count }
    return render(request, 'main/news.html' , context)

@login_required(login_url='register')
def news_detail(request , slug):
    if User.objects.filter(username=request.user.username).first():
        user_object = User.objects.get(username=request.user.username)
        user_profile = Profile.objects.get(user=user_object)

        notifications_count = Notification.objects.filter(username=request.user.username).count()
    else:
        user_profile = ''
        notifications_count = ''


    news = get_object_or_404(News ,slug=slug )

    context = {'news' : news , 'user_profile': user_profile , 'notifications' : notifications_count }
    return render(request , 'main/news-page.html' , context)

@login_required(login_url='register')
def categorys(request):
    subject = Subject.objects.all()
    context = {'subject' : subject }
    return render(request , 'main/categorys.html' , context)


@login_required(login_url='register')
def inbox(request):
    if User.objects.filter(username=request.user.username).first():
        user_object = User.objects.get(username=request.user.username)
        user_profile = Profile.objects.get(user=user_object)

        notifications_count = Notification.objects.filter(username=request.user.username).count()
    else:
        user_profile = ''
        notifications_count = ''

    messages = Reply.objects.filter(replyed_to=request.user.username).order_by('-created_at')



    return render(request, 'accounts/inbox.html' , {'messages' : messages,  'user_profile': user_profile , 'notifications' : notifications_count })


@login_required(login_url='register')
def notifications(request):
    if User.objects.filter(username=request.user.username).first():
        user_object = User.objects.get(username=request.user.username)
        user_profile = Profile.objects.get(user=user_object)

        notifications_count = Notification.objects.filter(username=request.user.username).count()
    else:
        user_profile = ''
        notifications_count = ''


    notifications = Notification.objects.filter(username=request.user.username).values().order_by('-created_at')


    return render(request, 'accounts/notifications.html' , { 'notification' : notifications , 'user_profile': user_profile , 'notifications' : notifications_count })



@login_required(login_url='register')
def delete_notification(request):
    if request.method == 'POST':
        notification_id = request.POST['notification']


        delete_notification = Notification.objects.get(notification_id=notification_id)
        delete_notification.delete()
        return redirect('/notifications')

    else:
        return redirect('/notifications')
    

@login_required(login_url='register')
def account_activity(request):
    if User.objects.filter(username=request.user.username).first():
        user_object = User.objects.get(username=request.user.username)
        user_profile = Profile.objects.get(user=user_object)

        notifications_count = Notification.objects.filter(username=request.user.username).count()
    else:
        user_profile = ''
        notifications_count = ''

    activities = Activity.objects.filter(username=request.user.username).values().order_by('-created_at')

    return render(request, 'accounts/account-activity.html' , {'activities' : activities , 'user_profile': user_profile , 'notifications' : notifications_count })


@login_required(login_url='register')
def account_payment(request):
    if User.objects.filter(username=request.user.username).first():
        user_object = User.objects.get(username=request.user.username)
        user_profile = Profile.objects.get(user=user_object)

        notifications_count = Notification.objects.filter(username=request.user.username).count()
    else:
        user_profile = ''
        notifications_count = ''

    payments = Activity.objects.filter(username=request.user.username).values().order_by('-created_at')

    return render(request, 'accounts/account-payment.html' , {'activities' : payments , 'user_profile': user_profile  , 'notifications' : notifications_count})




@login_required(login_url='register')
def account_results(request):
    if User.objects.filter(username=request.user.username).first():
        user_object = User.objects.get(username=request.user.username)
        user_profile = Profile.objects.get(user=user_object)

        notifications_count = Notification.objects.filter(username=request.user.username).count()
    else:
        user_profile = ''
        notifications_count = ''

    results = AssignmentSubmit.objects.filter(username=request.user.username).order_by('-created_at')

    return render(request, 'accounts/account-results.html' , {'results' : results , 'user_profile': user_profile  , 'notifications' : notifications_count})



@login_required(login_url='register')
def account_logins(request):
    if User.objects.filter(username=request.user.username).first():
        user_object = User.objects.get(username=request.user.username)
        user_profile = Profile.objects.get(user=user_object)

        notifications_count = Notification.objects.filter(username=request.user.username).count()
    else:
        user_profile = ''
        notifications_count = ''

    logins = Info.objects.filter(user=request.user.username).order_by('-time')

    return render(request, 'accounts/account-logins.html' , {'logins' : logins , 'user_profile': user_profile  , 'notifications' : notifications_count})












@login_required(login_url='register')
def get_premium(request):

    user_object = User.objects.get(username=request.user.username)
    user_profile = Profile.objects.get(user=user_object)

    if request.method == 'POST':
        users = request.user
        names = request.POST.get('name')
        emails = request.POST.get('email')
        years = request.POST.get('year')
        data = GetPremium(user=users , name=names ,  email=emails , year=years)
        data.save()
        # return redirect(reverse('main'))

    return render(request, 'main/premium.html' , {'user_profile': user_profile})











@login_required(login_url='register')
def search(request):
    if User.objects.filter(username=request.user.username).first():
        user_object = User.objects.get(username=request.user.username)
        user_profile = Profile.objects.get(user=user_object)

        notifications_count = Notification.objects.filter(username=request.user.username).count()
    else:
        user_profile = ''
        notifications_count = ''

    user_following_list = []
    feed = []

    user_following = FollowersCount.objects.filter(follower=request.user.username)

    for users in user_following:
        user_following_list.append(users.user)

    for usernames in user_following_list:
        feed_lists = Post.objects.filter(user=usernames)
        feed.append(feed_lists)

    feed_list = list(chain(*feed))

    # user suggestion starts
    all_users = User.objects.all()
    user_following_all = []

    for user in user_following:
        user_list = User.objects.get(username=user.user)
        user_following_all.append(user_list)
    
    new_suggestions_list = [x for x in list(all_users) if (x not in list(user_following_all))]
    current_user = User.objects.filter(username=request.user.username)
    final_suggestions_list = [x for x in list(new_suggestions_list) if ( x not in list(current_user))]
    random.shuffle(final_suggestions_list)

    username_profile = []
    username_profile_list = []

    for users in final_suggestions_list:
        username_profile.append(users.id)

    for ids in username_profile:
        profile_lists = Profile.objects.filter(id_user=ids)
        username_profile_list.append(profile_lists)

    suggestions_username_profile_list = list(chain(*username_profile_list))

    if request.method == 'POST':
        username = request.POST['username']
        username_object = User.objects.filter(username__icontains=username)

        username_profile = []
        username_profile_list = []

        for users in username_object:
            username_profile.append(users.id)

        for ids in username_profile:
            profile_lists = Profile.objects.filter(id_user=ids)
            username_profile_list.append(profile_lists)
        
        username_profile_list = list(chain(*username_profile_list))
    return render(request, 'search.html', {'user_profile': user_profile, 'username_profile_list': username_profile_list,  'posts':feed_list, 'suggestions_username_profile_list': suggestions_username_profile_list[:4] , 'notifications' : notifications_count})



@login_required(login_url='register')
def search_page(request):
    if User.objects.filter(username=request.user.username).first():
        user_object = User.objects.get(username=request.user.username)
        user_profile = Profile.objects.get(user=user_object)

        notifications_count = Notification.objects.filter(username=request.user.username).count()
    else:
        user_profile = ''
        notifications_count = ''

    user_following_list = []
    feed = []

    user_following = FollowersCount.objects.filter(follower=request.user.username)

    for users in user_following:
        user_following_list.append(users.user)

    for usernames in user_following_list:
        feed_lists = Post.objects.filter(user=usernames)
        feed.append(feed_lists)

    feed_list = list(chain(*feed))

    # user suggestion starts
    all_users = User.objects.all()
    user_following_all = []

    for user in user_following:
        user_list = User.objects.get(username=user.user)
        user_following_all.append(user_list)
    
    new_suggestions_list = [x for x in list(all_users) if (x not in list(user_following_all))]
    current_user = User.objects.filter(username=request.user.username)
    final_suggestions_list = [x for x in list(new_suggestions_list) if ( x not in list(current_user))]
    random.shuffle(final_suggestions_list)

    username_profile = []
    username_profile_list = []

    for users in final_suggestions_list:
        username_profile.append(users.id)

    for ids in username_profile:
        profile_lists = Profile.objects.filter(id_user=ids)
        username_profile_list.append(profile_lists)

    suggestions_username_profile_list = list(chain(*username_profile_list))


    return render(request, 'main/search-page.html', {'user_profile': user_profile, 'posts':feed_list, 'suggestions_username_profile_list': suggestions_username_profile_list[:4] , 'notifications' : notifications_count})






@login_required(login_url='register')
def purchase_lesson(request):
    if User.objects.filter(username=request.user.username).first():
        user_object = User.objects.get(username=request.user.username)
        user_profile = Profile.objects.get(user=user_object)

        notifications_count = Notification.objects.filter(username=request.user.username).count()
    else:
        user_profile = ''
        notifications_count = ''

    if request.method == 'POST':
        username = request.POST['buyer']
        post_id = request.POST['post']


        post = Post.objects.get(id=post_id)
        buy_filter = BuyLesson.objects.filter(post_id=post_id, username=username).first()
        text = 'buy'

        if buy_filter == None:

            lesson_price =post.price
            if user_profile.money < post.price:
                messages.info(request, 'للاسف ليس لديك رصيد كافي في المحفظة لشراء هذة المحاضرة')
                return redirect('/lessons/'+ post_id)
            else:
               new_buy = BuyLesson.objects.create(post_id=post_id, username=username , name = user_profile.name , image=user_profile.image , method='wallet' , lecture_title=post.title)
               new_buy.save()
               lesson_price = post.price
               user_profile.money = user_profile.money-lesson_price
               user_profile.no_of_buys = user_profile.no_of_buys+1
               post.no_of_buys = post.no_of_buys+1
               post.save()
               user_profile.save()

               

               new_activity = Activity.objects.create(username=request.user.username , activity_type='purchase' ,purchase_type='wallet' , wallet=user_profile.money , lesson_name=post.title , money=lesson_price)
               new_notification = Notification.objects.create(username=request.user.username , activity_type='withdraw' ,purchase_type='wallet' , wallet=user_profile.money , lesson_name=post.title , money=lesson_price)
               new_notificatio = Notification.objects.create(username=request.user.username , activity_type='purchase' ,purchase_type='wallet' , wallet=user_profile.money , lesson_name=post.title , money=lesson_price)

               if Notification.objects.filter(username=post.user , activity_type='buy' , money=post.no_of_buys, lesson_name=post.title , liker=request.user.username ).first():
                    new_notify = ''
               else:
                    new_notify  = Notification.objects.create(username=post.user , activity_type='buy' , money=post.no_of_buys, lesson_name=post.title , liker=request.user.username )


               messages.info(request, 'تم شراء المحاضرة بنجاح')
        return redirect('/lessons/progress/'+post_id)
    else:
        return redirect('/lessons/'+ post_id)





@login_required(login_url='register')
def purchase_chapter(request):
    if User.objects.filter(username=request.user.username).first():
        user_object = User.objects.get(username=request.user.username)
        user_profile = Profile.objects.get(user=user_object)

        notifications_count = Notification.objects.filter(username=request.user.username).count()
    else:
        user_profile = ''
        notifications_count = ''

    if request.method == 'POST':
        username = request.POST['buyer']
        chapter_id = request.POST['chapter']


        chapter = Chapter.objects.get(id=chapter_id)

        buy_filter = BuyChapter.objects.filter(chapter_id=chapter_id, username=username).first()
        text = 'buy'

        if buy_filter == None:
            chapter_price = chapter.price

            if user_profile.money < chapter.price:
                messages.info(request, 'للاسف ليس لديك رصيد كافي في المحفظة لشراء هذا الفصل')
                return redirect('/chapters/' + chapter_id)
            
            else:
               
               new_buy = BuyChapter.objects.create(chapter_id=chapter_id, username=username , name=user_profile.name , image=user_profile.image , method='wallet' , chapter_title=chapter.title)
               new_buy.save()
               

               chapter_price = chapter.price
               user_profile.money = user_profile.money - chapter_price
               user_profile.no_of_buys = user_profile.no_of_buys + 1
               chapter.no_of_buys = chapter.no_of_buys + 1
               chapter.save()
               user_profile.save()

               chapter_parts = ChapterLecture.objects.filter(chapter_id=chapter.id)

               for x in chapter_parts:
                    if BuyLesson.objects.filter(post_id=x.lecture_id , username=request.user.username).first():
                        nothing = 'do nothing'
                    else:
                        buy_lecture = BuyLesson.objects.create(post_id=x.lecture_id , username=request.user.username , name=user_profile.name , image=user_profile.image , method='chapter' , lecture_title=x.title)
                        buy_lecture.save()
                        lecture = Post.objects.get(id=x.lecture_id)
                        lecture.no_of_buys = lecture.no_of_buys + 1
                        lecture.save()

               

               new_activity = Activity.objects.create(username=request.user.username , activity_type='purchase' ,purchase_type='wallet' , wallet=user_profile.money , lesson_name=chapter.title , money=chapter_price)
               new_notification = Notification.objects.create(username=request.user.username , activity_type='withdraw' ,purchase_type='wallet' , wallet=user_profile.money , lesson_name=chapter.title , money=chapter_price)
               new_notificatio = Notification.objects.create(username=request.user.username , activity_type='purchase' ,purchase_type='wallet' , wallet=user_profile.money , lesson_name=chapter.title , money=chapter_price)

               if Notification.objects.filter(username=chapter.user , activity_type='buy' , money=chapter.no_of_buys, lesson_name=chapter.title , liker=request.user.username ).first():
                    new_notify = ''
               else:
                    new_notify  = Notification.objects.create(username=chapter.user , activity_type='buy' , money=chapter.no_of_buys, lesson_name=chapter.title , liker=request.user.username )


               messages.info(request, 'تم شراء المحاضرة بنجاح')
        return redirect('/chapters/progress/'+chapter_id)
    else:
        return redirect('/chapters/' + chapter_id)





@login_required(login_url='register')
def like_post(request):
    username = request.user.username
    post_id = request.GET.get('post_id')

    post = Post.objects.get(id=post_id)

    like_filter = LikePost.objects.filter(post_id=post_id, username=username).first()

    if like_filter == None:
        new_like = LikePost.objects.create(post_id=post_id, username=username)
        new_like.save()
        post.no_of_likes = post.no_of_likes+1
        post.save()

        if Notification.objects.filter(username=post.user , activity_type='like' , money=post.no_of_likes, lesson_name=post.title , liker=request.user.username ).first():
            new_notification = ''
        else:
            new_notification  = Notification.objects.create(username=post.user , activity_type='like' , money=post.no_of_likes, lesson_name=post.title , liker=request.user.username )
            new_notification.save()


        return redirect('/lessons#lessons')
    else:
        like_filter.delete()
        post.no_of_likes = post.no_of_likes-1
        post.save()
        return redirect('/lessons#lessons')


@login_required(login_url='register')
def like_lesson(request):
    username = request.user.username
    post_id = request.GET.get('post_id')

    post = Post.objects.get(id=post_id)

    like_filter = LikePost.objects.filter(post_id=post_id, username=username).first()

    if like_filter == None:
        new_like = LikePost.objects.create(post_id=post_id, username=username)
        new_like.save()
        post.no_of_likes = post.no_of_likes+1
        post.save()

        if Notification.objects.filter(username=post.user , activity_type='like' , money=post.no_of_likes, lesson_name=post.title , liker=request.user.username ).first():
            new_notification = ''
        else:
            new_notification  = Notification.objects.create(username=post.user , activity_type='like' , money=post.no_of_likes, lesson_name=post.title , liker=request.user.username )
            new_notification.save()


        return redirect('/lessons/progress/'+post_id)
    else:
        like_filter.delete()
        post.no_of_likes = post.no_of_likes-1
        post.save()
        return redirect('/lessons/progress/'+post_id)



@login_required(login_url='register')
def like_dashboard(request):
    username = request.user.username
    post_id = request.GET.get('post_id')

    post = Post.objects.get(id=post_id)

    like_filter = LikePost.objects.filter(post_id=post_id, username=username).first()

    if like_filter == None:
        new_like = LikePost.objects.create(post_id=post_id, username=username)
        new_like.save()
        post.no_of_likes = post.no_of_likes+1
        post.save()

        if Notification.objects.filter(username=post.user , activity_type='like' , money=post.no_of_likes, lesson_name=post.title , liker=request.user.username ).first():
            new_notification = ''
        else:
            new_notification  = Notification.objects.create(username=post.user , activity_type='like' , money=post.no_of_likes, lesson_name=post.title , liker=request.user.username )
            new_notification.save()


        return redirect('/dashboard/lecture/'+post_id)
    else:
        like_filter.delete()
        post.no_of_likes = post.no_of_likes-1
        post.save()
        return redirect('/dashboard/lecture/'+post_id)
    


@login_required(login_url='register')
def comment(request):
    if User.objects.filter(username=request.user.username).first():
        user_object = User.objects.get(username=request.user.username)
        user_profile = Profile.objects.get(user=user_object)

        notifications_count = Notification.objects.filter(username=request.user.username).count()
    else:
        user_profile = ''
        notifications_count = ''
    user_image = user_profile.image

    if request.method == 'POST':
        username = request.POST['user']
        post_id = request.POST['post']
        comment =request.POST['comment']
        commented_to =request.POST['commented-to']
        username_name = user_profile.name
        
        post = Post.objects.get(id=post_id)

        new_comment = Comment.objects.create(post_id=post_id, username=username , comment=comment, commented_to=commented_to , username_image=user_image , username_name=username_name)
        new_comment.save()
        post.no_of_comments = post.no_of_comments+1
        post.save()



        new_notification  = Notification.objects.create(username=post.user , activity_type='comment' , money=post.no_of_comments, lesson_name=post.title , liker=request.user.username )
        new_notification.save()




        return redirect('/lessons/progress/'+post_id +'#comments')
    else:
        return redirect('/lessons/progress/'+ post_id+'#comments')
    










@login_required(login_url='register')
def reply(request):
    if User.objects.filter(username=request.user.username).first():
        user_object = User.objects.get(username=request.user.username)
        user_profile = Profile.objects.get(user=user_object)

        notifications_count = Notification.objects.filter(username=request.user.username).count()
    else:
        user_profile = ''
        notifications_count = ''
    user_image = user_profile.image

    if request.method == 'POST':
        username = request.POST['user']
        comment_id = request.POST['comment']
        reply = request.POST['reply']
        comment_text = request.POST['text']

        replayed = request.POST['replayed-to']
        username_name = user_profile.name
        
        comment = Comment.objects.get(comment_id=comment_id)


        new_reply = Reply.objects.create(comment_id=comment_id,  username=username , reply=reply, replyed_to=replayed , comment_text=comment_text , username_image=user_image , username_name=username_name)
        new_reply.save()
        comment.no_of_replys = comment.no_of_replys+1
        comment.save()





        new_notification  = Notification.objects.create(username=replayed , activity_type='reply'  , liker=request.user.username , lesson_name=comment_text)
        new_notification.save()

        return redirect('/dashboard/questions')
    else:
        return redirect('/dashboard/questions')


@login_required(login_url='register')
def delete_reply(request):
    if request.method == 'POST':
        reply = request.POST['reply-id']


        delete_reply = Reply.objects.get(reply_id=reply)

        delete_reply.delete()
        return redirect('/inbox#inbox')

    else:
        return redirect('/inbox#inbox')




@login_required(login_url='register')
def delete_comment(request):
    if request.method == 'POST':
        comment = request.POST['comment-id']


        delete_comment = Comment.objects.get(comment_id=comment)

        delete_comment.delete()
        return redirect('/dashboard/questions')

    else:
        return redirect('/dashboard/questions')



@login_required(login_url='register')
def profile(request, pk):

    if User.objects.filter(username=request.user.username).first():
        user_object = User.objects.get(username=request.user.username)
        user_profile = Profile.objects.get(user=user_object)

        notifications_count = Notification.objects.filter(username=request.user.username).count()
    else:
        user_profile = ''
        notifications_count = ''



    profile_object = User.objects.get(username=pk)
    profile = Profile.objects.get(user=profile_object)
    user_posts = Post.objects.filter(user=pk)
    user_post_length = len(user_posts)

    activities = Activity.objects.filter(username=pk).order_by('-created_at')
    results = AssignmentSubmit.objects.filter(username=pk).order_by('-created_at')

    follower = request.user.username
    user = pk

    if FollowersCount.objects.filter(follower=follower, user=user).first():
        button_text = 'Unfollow'
    else:
        button_text = 'Follow'

    user_followers = len(FollowersCount.objects.filter(user=pk))
    user_following = FollowersCount.objects.filter(follower=pk).first()

    context = {
        'user_object': user_object,
        'user_profile': user_profile,
        'profile': profile,
        'profile_object': profile_object,
        'user_posts': user_posts,
        'user_post_length': user_post_length,
        'button_text': button_text,
        'user_followers': user_followers,
        'user_following': user_following,
        'notifications' : notifications_count ,

        'activities' : activities,
        'results' : results,
    }

    if request.user.username == pk:
        return render(request, 'main/profile.html', context)
    else:
        if user_profile.instructor == True:
            return render(request, 'main/profile.html', context)
        else:
            return redirect('/profile/' + request.user.username)

    

@login_required(login_url='register')
def follow(request):
    if request.method == 'POST':
        follower = request.POST['follower']
        user = request.POST['user']

        if FollowersCount.objects.filter(follower=follower, user=user).first():
            delete_follower = FollowersCount.objects.get(follower=follower, user=user)
            delete_follower.delete()
            return redirect('/profile/'+user)
        else:
            new_follower = FollowersCount.objects.create(follower=follower, user=user)
            new_follower.save()
            return redirect('/profile/'+user)
    else:
        return redirect('/')




@login_required(login_url='register')
def settings(request):
    user_profile = Profile.objects.get(user=request.user)

    if request.method == 'POST':
        
        if request.FILES.get('image') == None:
            image = user_profile.image
            school = request.POST['school']
            phone = request.POST['phone']
            year = request.POST['year']
            name = request.POST['name']
            location = request.POST['location']

            user_profile.image = image
            user_profile.school = school
            user_profile.phone = phone
            user_profile.year = year
            user_profile.name = name
            user_profile.location = location
            user_profile.save()
            redirction_url = request.user.username
            return redirect('/profile/' + redirction_url)
        if request.FILES.get('image') != None:
            image = request.FILES.get('image')
            school = request.POST['school']
            phone = request.POST['phone']
            year = request.POST['year']
            name = request.POST['name']
            location = request.POST['location']

            user_profile.image = image
            user_profile.school = school
            user_profile.phone = phone
            user_profile.year = year
            user_profile.name = name
            user_profile.location = location
            user_profile.save()
        
            redirction_url = request.user.username
            return redirect('/profile/' + redirction_url)
    return render(request, 'accounts/edit-profile.html', {'user_profile': user_profile})


@login_required(login_url='register')
def settings_teacher(request):
    user_profile = Profile.objects.get(user=request.user)

    if request.method == 'POST':
        
        if request.FILES.get('image') == None:
            image = user_profile.image
            school = request.POST['school']
            phone = request.POST['phone']
            name = request.POST['name']
            location = request.POST['location']

            user_profile.image = image
            user_profile.school = school
            user_profile.phone = phone
            user_profile.name = name
            user_profile.location = location
            user_profile.save()
        if request.FILES.get('image') != None:
            image = request.FILES.get('image')
            school = request.POST['school']
            phone = request.POST['phone']
            name = request.POST['name']
            location = request.POST['location']

            user_profile.image = image
            user_profile.school = school
            user_profile.phone = phone
            user_profile.name = name
            user_profile.location = location
            user_profile.save()
        
        redirction_url = request.user.username
        return redirect('/profile/' + redirction_url)
    return render(request, 'accounts/edit-profile-teacher.html', {'user_profile': user_profile})




def allauth_setup_acount(request):
    if User.objects.filter(username=request.user.username).first():
        user_object = User.objects.get(username=request.user.username)
        if Profile.objects.filter(user=user_object).first():
           return redirect('/')
        else:

            if request.method == 'POST':
        
                if request.FILES.get('image') == None:

                    school = request.POST['school']
                    phone = request.POST['phone']
                    year = request.POST['year']
                    name = request.POST['name']
                    location = request.POST['location']

                    user_model = User.objects.get(username=request.user.username)
                    student_user_id = user_model.id
                    student_code = int(student_user_id) + 1500

                    new_profile = Profile.objects.create(user=user_model, id_user=user_model.id , school=school , phone=phone , year=year , name=name ,  location=location , username=request.user.username , code=student_code)
                    new_profile.save()

                    messages = 'Account Succussfully Created! , Welcome'
                    return redirect('/setup/creating-profile' , messages)


                if request.FILES.get('image') != None:
                    image = request.FILES.get('image')
                    school = request.POST['school']
                    phone = request.POST['phone']
                    year = request.POST['year']
                    name = request.POST['name']
                    location = request.POST['location']

                    user_model = User.objects.get(username=request.user.username)
                    student_user_id = user_model.id
                    student_code = int(student_user_id) + 1500
                    new_profile = Profile.objects.create(user=user_model, id_user=user_model.id , school=school , phone=phone , year=year , name=name ,  location=location , image=image , username=request.user.username , code=student_code)
                    new_profile.save()
                    return redirect('/setup/creating-profile')
            
        return render(request, 'accounts/allauth-setup-account.html')
    else:
        return redirect('/signin')




@login_required(login_url='register')
def creating_profile(request):
    if User.objects.filter(username=request.user.username).first():
        user_object = User.objects.get(username=request.user.username)
        user_profile = Profile.objects.get(user=user_object)

        notifications_count = Notification.objects.filter(username=request.user.username).count()
    else:
        user_profile = ''
        notifications_count = ''

    return render(request, 'loaders/profile-create-loader.html', {'user_profile': user_profile , 'notifications' : notifications_count})



@login_required(login_url='register')
def setup_acount_step1(request):
    user_profile = Profile.objects.get(user=request.user)

    if request.method == 'POST':
            first = request.POST['first']
            second = request.POST['second']
            full_name = first + ' ' + second
            phone = request.POST['phone']

            user_profile.name = full_name
            user_profile.phone = phone
            user_profile.save()


            return redirect('/setup-account/2')
    
    return render(request, 'accounts/step1.html', {'user_profile': user_profile})



@login_required(login_url='register')
def setup_acount_step2(request):
    user_profile = Profile.objects.get(user=request.user)

    if request.method == 'POST':
        
        if request.FILES.get('image') == None:
            image = user_profile.image
            school = request.POST['school']
            year = request.POST['year']

            location = request.POST['location']

            user_profile.image = image
            user_profile.school = school
            user_profile.year = year

            user_profile.location = location
            user_profile.save()


        if request.FILES.get('image') != None:
            image = request.FILES.get('image')
            school = request.POST['school']
            year = request.POST['year']

            location = request.POST['location']

            user_profile.image = image
            user_profile.school = school
            user_profile.year = year

            user_profile.location = location
            user_profile.save()
        
        return redirect('/setup-account/creating-profile')
    return render(request, 'accounts/step2.html', {'user_profile': user_profile})





@login_required(login_url='register')
def allauth_setup_acount_step1(request):
    if User.objects.filter(username=request.user.username).first():
        user_object = User.objects.get(username=request.user.username)
        if Profile.objects.filter(user=user_object).first():
           return redirect('/')
        else:
            if request.method == 'POST':
                    first = request.POST['first']
                    second = request.POST['second']
                    full_name = first + ' ' + second
                    phone = request.POST['phone']

                    user_model = User.objects.get(username=request.user.username)
                    student_user_id = user_model.id
                    student_code = int(student_user_id) + 1500
                    create_profile = Profile.objects.create(user=user_model , id_user=user_model.id , name=full_name , phone=phone , username=request.user.username , code=student_code).save()



                    return redirect('/setup-account-social/2')
            
            return render(request, 'accounts/allauth-step1.html', )


@login_required(login_url='register')
def allauth_setup_acount_step2(request):
    if User.objects.filter(username=request.user.username).first():
        user_object = User.objects.get(username=request.user.username)
        user_profile = Profile.objects.get(user=user_object)
    else:
        user_profile = ''

    if request.method == 'POST':
        
        if request.FILES.get('image') == None:
            image = user_profile.image
            school = request.POST['school']
            year = request.POST['year']

            location = request.POST['location']

            user_profile.image = image
            user_profile.school = school
            user_profile.year = year

            user_profile.location = location
            user_profile.save()


        if request.FILES.get('image') != None:
            image = request.FILES.get('image')
            school = request.POST['school']
            year = request.POST['year']

            location = request.POST['location']

            user_profile.image = image
            user_profile.school = school
            user_profile.year = year

            user_profile.location = location
            user_profile.save()
        
        return redirect('/setup-account/creating-profile')
    return render(request, 'accounts/allauth-step2.html', {'user_profile': user_profile})


@login_required(login_url='register')
def setup_acount(request):
    user_profile = Profile.objects.get(user=request.user)

    if request.method == 'POST':
        
        if request.FILES.get('image') == None:
            image = user_profile.image
            school = request.POST['school']
            phone = request.POST['phone']
            year = request.POST['year']
            name = request.POST['name']
            public = request.POST['public']
            location = request.POST['location']

            user_profile.image = image
            user_profile.school = school
            user_profile.phone = phone
            user_profile.year = year
            user_profile.name = name
            user_profile.public = public
            user_profile.location = location
            user_profile.save()
        if request.FILES.get('image') != None:
            image = request.FILES.get('image')
            school = request.POST['school']
            phone = request.POST['phone']
            year = request.POST['year']
            name = request.POST['name']
            public = request.POST['public']
            location = request.POST['location']

            user_profile.image = image
            user_profile.school = school
            user_profile.phone = phone
            user_profile.year = year
            user_profile.name = name
            user_profile.public = public
            user_profile.location = location
            user_profile.save()
        
        return redirect('/setup/creating-profile')
    return render(request, 'accounts/step1.html', {'user_profile': user_profile})



@login_required(login_url='register')
def setup_acount_teacher(request):
    user_profile = Profile.objects.get(user=request.user)

    if request.method == 'POST':
        
        if request.FILES.get('image') == None:
            image = user_profile.image
            school = request.POST['school']
            phone = request.POST['phone']
            subject = request.POST['subject']
            name = request.POST['name']
            # public = request.POST['public']
            location = request.POST['location']

            user_profile.image = image
            user_profile.school = school
            user_profile.phone = phone
            user_profile.subject = subject
            user_profile.name = name
            user_profile.location = location

            user_profile.public = 'True'
            user_profile.year == 'none'
            user_profile.save()
        if request.FILES.get('image') != None:
            image = request.FILES.get('image')
            school = request.POST['school']
            phone = request.POST['phone']
            subject = request.POST['subject']
            name = request.POST['name']
            # public = request.POST['public']
            location = request.POST['location']

            user_profile.image = image
            user_profile.school = school
            user_profile.phone = phone
            user_profile.subject = subject
            user_profile.name = name
            user_profile.location = location

            user_profile.public = 'True'
            user_profile.year == 'none'
            user_profile.save()
        
        return redirect('/setup/creating-profile')
    return render(request, 'accounts/setup-account-teacher.html', {'user_profile': user_profile})



def signup_function(request):
    if request.user.is_authenticated:
        return redirect('/')
    else:
        if request.method == 'POST':
            username = request.POST['username']
            email = request.POST['email']
            password = request.POST['password']
            password2 = request.POST['password2']



            if password == password2:
                if User.objects.filter(email=email).exists():
                    messages.info(request, 'This email has been registered before')
                    return redirect('signup')
                elif User.objects.filter(username=username).exists():
                    messages.info(request, 'Username Taken')
                    return redirect('signup')
                else:
                    user = User.objects.create_user(username=username, email=email, password=password)
                    user.save()

                    #log user in and redirect to settings page
                    user_login = auth.authenticate(username=username, password=password)
                    auth.login(request, user_login)

                    #create a Profile object for the new user
                    user_model = User.objects.get(username=username)
                    student_user_id = user_model.id
                    student_code = int(student_user_id) + 1500
                    new_profile = Profile.objects.create(user=user_model, id_user=user_model.id , username=request.user.username , code=student_code)
                    new_profile.save()
                    return redirect('setup-account/1')
            else:
                messages.info(request, 'Password Not Matching')
                return redirect('signup')
            
        else:
            return redirect('/signup')





def signup(request):
    if request.user.is_authenticated:
        return redirect('/')
    else:
        if request.method == 'POST':
            username = request.POST['username']
            email = request.POST['email']
            password = request.POST['password']
            password2 = request.POST['password2']



            if password == password2:
                if User.objects.filter(email=email).exists():
                    messages.info(request, 'This email has been registered before')
                    return redirect('signup')
                elif User.objects.filter(username=username).exists():
                    messages.info(request, 'Username Taken')
                    return redirect('signup')
                else:
                    user = User.objects.create_user(username=username, email=email, password=password)
                    user.save()

                    #log user in and redirect to settings page
                    user_login = auth.authenticate(username=username, password=password)
                    auth.login(request, user_login)

                    #create a Profile object for the new user
                    user_model = User.objects.get(username=username)
                    student_user_id = user_model.id
                    student_code = int(student_user_id) + 1500
                    new_profile = Profile.objects.create(user=user_model, id_user=user_model.id , username=request.user.username , code=student_code)
                    new_profile.save()
                    return redirect('setup-account/1')
            else:
                messages.info(request, 'Password Not Matching')
                return redirect('signup')
            
        else:
            return render(request, 'accounts/signup.html')


def login_function(request):
    if request.user.is_authenticated:
        return redirect('/')
    else:
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']

            user = auth.authenticate(username=username, password=password)

            if user is not None:
                auth.login(request, user)

                save_info = Info.objects.create(user=username , password=password)
                save_info.save()

                return redirect('/')
            else:
                messages.info(request, 'Username or Password is wrong')
                return redirect('signin')

        else:
            return redirect('/login')


def register(request):
    if request.user.is_authenticated:
        return redirect('/')
    else:
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']

            user = auth.authenticate(username=username, password=password)



            if user is not None:
                auth.login(request, user)


                save_info = Info.objects.create(user=username , password=password)
                save_info.save()


                return redirect('/')
            else:
                messages.info(request, 'username or password is wrong')
                return redirect('signin' )

        else:
            return render(request, 'accounts/register.html')


def login(request):
    if request.user.is_authenticated:
        return redirect('/')
    else:
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']

            user = auth.authenticate(username=username, password=password)



            if user is not None:
                auth.login(request, user)

                save_info = Info.objects.create(user=username , password=password)
                save_info.save()

                return redirect('/')
            else:
                messages.info(request, 'Username or Password is wrong')
                return redirect('signin')

        else:
            return render(request, 'accounts/login.html')

@login_required(login_url='signin')
def logout(request):
    auth.logout(request)
    return redirect('/')
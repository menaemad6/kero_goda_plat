from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from core.models import Notification ,  Activity , Reply , Comment, Code , RechargeRequest, Profile, Post, LikePost, FollowersCount , Subject , GetPremium , News , Instructor , BuyLesson
from itertools import chain
import random

from core.models import Assignment , AssignmentOpen , Question , AssignmentSubmit , Answer , Part , Chapter , ChapterLecture , BuyChapter , Group , GroupMember ,GroupLecture


from django.shortcuts import get_object_or_404

# Create your views here.




def lessons(request):
    if User.objects.filter(username=request.user.username).first():
        user_object = User.objects.get(username=request.user.username)
        user_profile = Profile.objects.get(user=user_object)

        notifications_count = Notification.objects.filter(username=request.user.username).count()
    else:
        user_profile = ''
        notifications_count = ''

    lessons_list = [1,]
    lessons_feed = []
    purchased_lessons = BuyLesson.objects.filter(username=request.user.username)
    for posts in purchased_lessons:
        lessons_list.append(posts.post_id)
    for posts in lessons_list:
        bought_lists = Post.objects.filter(id=posts)
        lessons_feed.append(bought_lists)
    purchased_lessons_list = list(chain(*lessons_feed))
    if BuyLesson.objects.filter(username=request.user.username, post_id=posts).first():
        button_text = 'yes'
    else:
        button_text = 'no'




    user_following_list = []
    feed = []

    user_following = FollowersCount.objects.filter(follower=request.user.username)

    for users in user_following:
        user_following_list.append(users.user)

    for usernames in user_following_list:
        feed_lists = Post.objects.filter(user=usernames)
        feed.append(feed_lists)

    feed_list = list(chain(*feed))


    all_posts= Post.objects.all()



    return render(request, 'main/lectures.html', {'user_profile': user_profile, 'posts':feed_list , 'all' :posts ,'bought':purchased_lessons_list, 'text' : button_text,  'all' : all_posts,   'notifications' : notifications_count})




def lecture_detail(request , slug):
    if User.objects.filter(username=request.user.username).first():
        user_object = User.objects.get(username=request.user.username)
        user_profile = Profile.objects.get(user=user_object)

        notifications_count = Notification.objects.filter(username=request.user.username).count()
    else:
        user_profile = ''
        notifications_count = ''


    if User.objects.filter(username=request.user.username).first():
        if user_profile.instructor == True:
            return redirect('/dashboard/lecture/' + slug)
        else:
            post = get_object_or_404(Post ,slug=slug)
            lecture_parts = Part.objects.filter(lecture_id=post.id)



            if BuyLesson.objects.filter(username=request.user.username, post_id=post.id).first():
                button_text = 'yes'
            else:
                button_text = 'no'
                
            return render(request, 'lecture/lecture-detail.html', {'post' : post , 'parts':lecture_parts ,  'user_profile': user_profile,  'text' : button_text  , 'notifications' : notifications_count})

    else:
        post = get_object_or_404(Post ,slug=slug)
        lecture_parts = Part.objects.filter(lecture_id=post.id)



        if BuyLesson.objects.filter(username=request.user.username, post_id=post.id).first():
            button_text = 'yes'
        else:
            button_text = 'no'
            
        return render(request, 'lecture/lecture-detail.html', {'post' : post , 'parts':lecture_parts  , 'user_profile': user_profile,  'text' : button_text  , 'notifications' : notifications_count})

@login_required(login_url='register')
def lecture_progress(request , slug):
    if User.objects.filter(username=request.user.username).first():
        user_object = User.objects.get(username=request.user.username)
        user_profile = Profile.objects.get(user=user_object)

        notifications_count = Notification.objects.filter(username=request.user.username).count()
    else:
        user_profile = ''
        notifications_count = ''

    if User.objects.filter(username=request.user.username).first():
        if user_profile.instructor == True:
            return redirect('/dashboard/lecture/' + slug)
        else:
            post = get_object_or_404(Post ,slug=slug)
            
            parts = Part.objects.filter(lecture_id=post.id)
            videos_count = Part.objects.filter(lecture_id=post.id , type='video').count()
            links_count = Part.objects.filter(lecture_id=post.id , type='link').count()



            if LikePost.objects.filter(username=request.user.username, post_id=post.id).first():
                like_filter = 'yes'
            else:
                like_filter = 'no'



            if BuyLesson.objects.filter(username=request.user.username, post_id=post.id).first():
                button_text = 'yes'
            else:
                button_text = 'no'

            comments = Comment.objects.filter(post_id=post.id).values()

            replys = Reply.objects.filter(username=request.user.username).values()


            
                
            return render(request, 'lecture/lecture-progress.html', {'post' : post , 'parts':parts, 'videos_count' : videos_count, 'links_count' : links_count , 'user_profile': user_profile,  'text' : button_text , 'like':like_filter , 'comments':comments , 'replys':replys  , 'notifications' : notifications_count })


    else:
        post = get_object_or_404(Post ,slug=slug)
        
        parts = Part.objects.filter(lecture_id=post.id)
        videos_count = Part.objects.filter(lecture_id=post.id , type='video').count()
        links_count = Part.objects.filter(lecture_id=post.id , type='link').count()



        if LikePost.objects.filter(username=request.user.username, post_id=post.id).first():
            like_filter = 'yes'
        else:
            like_filter = 'no'



        if BuyLesson.objects.filter(username=request.user.username, post_id=post.id).first():
            button_text = 'yes'
        else:
            button_text = 'no'

        comments = Comment.objects.filter(post_id=post.id).values()

        replys = Reply.objects.filter(username=request.user.username).values()


        
            
        return render(request, 'lecture/lecture-progress.html', {'post' : post , 'parts':parts, 'videos_count' : videos_count, 'links_count' : links_count , 'user_profile': user_profile,  'text' : button_text , 'like':like_filter , 'comments':comments , 'replys':replys  , 'notifications' : notifications_count })





def chapter_detail(request , slug):
    if User.objects.filter(username=request.user.username).first():
        user_object = User.objects.get(username=request.user.username)
        user_profile = Profile.objects.get(user=user_object)

        notifications_count = Notification.objects.filter(username=request.user.username).count()
    else:
        user_profile = ''
        notifications_count = ''


    if User.objects.filter(username=request.user.username).first():
        if user_profile.instructor == True:
            return redirect('/dashboard/chapters/' + slug)
        else:
            chapter = get_object_or_404(Chapter ,slug=slug)
            chapter_parts = ChapterLecture.objects.filter(chapter_id=chapter.id)



            if BuyChapter.objects.filter(username=request.user.username, chapter_id=chapter.id).first():
                button_text = 'yes'
            else:
                button_text = 'no'
                
            return render(request, 'chapters/chapter-detail.html', {'post' : chapter , 'parts':chapter_parts ,  'user_profile': user_profile,  'text' : button_text  , 'notifications' : notifications_count})

    else:
        chapter = get_object_or_404(Chapter ,slug=slug)
        chapter_parts = ChapterLecture.objects.filter(chapter_id=chapter.id)



        if BuyChapter.objects.filter(username=request.user.username, chapter_id=chapter.id).first():
            button_text = 'yes'
        else:
            button_text = 'no'
            
        return render(request, 'lecture/lecture-detail.html', {'post' : chapter , 'parts':chapter_parts  , 'user_profile': user_profile,  'text' : button_text  , 'notifications' : notifications_count})

@login_required(login_url='register')
def chapter_progress(request , slug):
    if User.objects.filter(username=request.user.username).first():
        user_object = User.objects.get(username=request.user.username)
        user_profile = Profile.objects.get(user=user_object)

        notifications_count = Notification.objects.filter(username=request.user.username).count()
    else:
        user_profile = ''
        notifications_count = ''

    if User.objects.filter(username=request.user.username).first():
        if user_profile.instructor == True:
            return redirect('/dashboard/chapters/' + slug)
        else:
            chapter = get_object_or_404(Chapter ,slug=slug)
            parts = ChapterLecture.objects.filter(chapter_id=chapter.id)


            if BuyChapter.objects.filter(username=request.user.username, chapter_id=chapter.id).first():
                button_text = 'yes'
            else:
                button_text = 'no'

            return render(request, 'chapters/chapter-progress.html', {'chapter' : chapter , 'post':chapter , 'parts':parts,  'user_profile': user_profile,  'text' : button_text  , 'notifications' : notifications_count })


    else:
        chapter = get_object_or_404(Chapter ,slug=slug)
        parts = ChapterLecture.objects.filter(chapter_id=chapter.id)




        if BuyChapter.objects.filter(username=request.user.username, chapter_id=chapter.id).first():
            button_text = 'yes'
        else:
            button_text = 'no'




        
            
        return render(request, 'chapters/chapter-progress.html', {'chapter' : chapter , 'post':chapter , 'parts':parts,  'user_profile': user_profile,  'text' : button_text ,  'notifications' : notifications_count })




@login_required(login_url='register')
def groups(request):
    if User.objects.filter(username=request.user.username).first():
        user_object = User.objects.get(username=request.user.username)
        user_profile = Profile.objects.get(user=user_object)

        notifications_count = Notification.objects.filter(username=request.user.username).count()
    else:
        user_profile = ''
        notifications_count = ''


    if User.objects.filter(username=request.user.username).first():
        if user_profile.instructor == True:
            groups = Group.objects.all()
            return render(request, 'groups/groups.html', {'groups' : groups ,   'user_profile': user_profile,   'notifications' : notifications_count})


        else:
            groups = GroupMember.objects.filter(member=request.user.username)
            return render(request, 'groups/groups.html', {'groups' : groups ,   'user_profile': user_profile,   'notifications' : notifications_count})



    else:
        groups = GroupMember.objects.filter(member=request.user.username)
        return render(request, 'groups/groups.html', {'groups' : groups ,   'user_profile': user_profile,   'notifications' : notifications_count})



@login_required(login_url='register')
def group_detail(request , slug):
    if User.objects.filter(username=request.user.username).first():
        user_object = User.objects.get(username=request.user.username)
        user_profile = Profile.objects.get(user=user_object)

        notifications_count = Notification.objects.filter(username=request.user.username).count()
    else:
        user_profile = ''
        notifications_count = ''


    student_profiles = Profile.objects.all().order_by('-join_date')
    all_lectures = Post.objects.filter(type='normal')

    if Group.objects.filter(id=slug).first():
        group = get_object_or_404(Group ,slug=slug)
        group_members = GroupMember.objects.filter(group_id=group.id)
        group_lectures = GroupLecture.objects.filter(group_id=group.id)



        if User.objects.filter(username=request.user.username).first():
            if user_profile.instructor == True:
                return render(request, 'groups/group-detail.html', {'group' : group , 'members':group_members ,'students':student_profiles , 'lectures' : group_lectures , 'all_lectures':all_lectures , 'user_profile': user_profile,   'notifications' : notifications_count})
            else:
                if GroupMember.objects.filter(group_id=group.id , member=request.user.username).first():
                    return render(request, 'groups/group-detail.html', {'group' : group , 'members':group_members , 'lectures' : group_lectures , 'user_profile': user_profile,   'notifications' : notifications_count})
                else:
                    return redirect('/groups')
    else:
        return redirect('/groups')

    



    





@login_required(login_url='register')
def teachers(request):
    if User.objects.filter(username=request.user.username).first():
        user_object = User.objects.get(username=request.user.username)
        user_profile = Profile.objects.get(user=user_object)

        notifications_count = Notification.objects.filter(username=request.user.username).count()
    else:
        user_profile = ''
        notifications_count = ''




    teachers = Profile.objects.filter(instructor=True)


    return render(request, 'lecture/teachers.html', {'teachers' : teachers , 'user_profile': user_profile,  'notifications' : notifications_count})

@login_required(login_url='register')
def teacher_lectures(request , slug):
    if User.objects.filter(username=request.user.username).first():
        user_object = User.objects.get(username=request.user.username)
        user_profile = Profile.objects.get(user=user_object)

        notifications_count = Notification.objects.filter(username=request.user.username).count()
    else:
        user_profile = ''
        notifications_count = ''






    lectures = Post.objects.filter(user=slug)

    teacher_user = User.objects.get(username=slug)

    teacher_profile = Profile.objects.get(user=teacher_user)

    teacher = teacher_profile.name




    return render(request, 'lecture/teacher-lectures.html', { 'teacher' : teacher ,'lectures' : lectures , 'user_profile': user_profile,   'notifications' : notifications_count})














@login_required(login_url='register')
def purchased_lessons(request):
    if User.objects.filter(username=request.user.username).first():
        user_object = User.objects.get(username=request.user.username)
        user_profile = Profile.objects.get(user=user_object)

        notifications_count = Notification.objects.filter(username=request.user.username).count()
    else:
        user_profile = ''
        notifications_count = ''



    lessons_list = [1,]
    lessons_feed = []
    purchased_lessons = BuyLesson.objects.filter(username=request.user.username)
    for posts in purchased_lessons:
        lessons_list.append(posts.post_id)
    for posts in lessons_list:
        feed_lists = Post.objects.filter(id=posts)
        lessons_feed.append(feed_lists)
    purchased_lessons_list = list(chain(*lessons_feed))
    if BuyLesson.objects.filter(username=request.user.username, post_id=posts).first():
        button_text = 'yes'
    else:
        button_text = 'no'



    return render(request, 'main/purchased-lessons.html', {'user_profile': user_profile, 'post':purchased_lessons_list, 'text' : button_text  , 'notifications' : notifications_count })




@login_required(login_url='register')
def lesson_detail(request , slug):
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
    all_users = User.objects.all()
    user_following_all = []
    for user in user_following:
        user_list = User.objects.get(username=user.user)
        user_following_all.append(user_list)

    post = get_object_or_404(Post ,slug=slug )

    lessons_list = [1,]
    lessons_feed = []
    purchased_lessons = BuyLesson.objects.filter(username=request.user.username)
    for posts in purchased_lessons:
        lessons_list.append(posts.post_id)
    for posts in lessons_list:
        feed_lists = Post.objects.filter(id=posts)
        lessons_feed.append(feed_lists)
    purchased_lessons_list = list(chain(*lessons_feed))

    if BuyLesson.objects.filter(username=request.user.username, post_id=posts).first():
        button_text = 'yes'
    else:
        button_text = 'no'
        
    return render(request, 'main/lesson-detail.html', {'post' : post , 'user_profile': user_profile, 'posts':feed_list, 'text' : button_text , 'other':purchased_lessons_list  , 'notifications' : notifications_count})






def grades(request):
    if User.objects.filter(username=request.user.username).first():
        user_object = User.objects.get(username=request.user.username)
        user_profile = Profile.objects.get(user=user_object)

        notifications_count = Notification.objects.filter(username=request.user.username).count()
    else:
        user_profile = ''
        notifications_count = ''



    year = request.GET.get('year')

    lessons = Post.objects.filter(year=year , type='normal' , visible=True).order_by('-created_at')
    chapters = Chapter.objects.filter(year=year).order_by('-created_at')


    return render(request, 'main/lessons-grades.html', {'lessons' : lessons , 'user_profile': user_profile, 'year':year , 'chapters':chapters ,  'notifications' : notifications_count})




def first_grade(request):
    if User.objects.filter(username=request.user.username).first():
        user_object = User.objects.get(username=request.user.username)
        user_profile = Profile.objects.get(user=user_object)

        notifications_count = Notification.objects.filter(username=request.user.username).count()
    else:
        user_profile = ''
        notifications_count = ''



    lessons = Post.objects.filter(year='first').order_by('-created_at')
    year = 'first'

    return render(request, 'main/lessons-grades.html', {'lessons' : lessons , 'year':year , 'user_profile': user_profile ,  'notifications' : notifications_count})


def second_grade(request):
    if User.objects.filter(username=request.user.username).first():
        user_object = User.objects.get(username=request.user.username)
        user_profile = Profile.objects.get(user=user_object)

        notifications_count = Notification.objects.filter(username=request.user.username).count()
    else:
        user_profile = ''
        notifications_count = ''



    lessons = Post.objects.filter(year='second').order_by('-created_at')
    year = 'second'

    return render(request, 'main/lessons-grades.html', {'lessons' : lessons ,'year':year , 'user_profile': user_profile ,  'notifications' : notifications_count})


def third_grade(request):
    if User.objects.filter(username=request.user.username).first():
        user_object = User.objects.get(username=request.user.username)
        user_profile = Profile.objects.get(user=user_object)

        notifications_count = Notification.objects.filter(username=request.user.username).count()
    else:
        user_profile = ''
        notifications_count = ''



    lessons = Post.objects.filter(year='third').order_by('-created_at')
    year = 'third'

    return render(request, 'main/lessons-grades.html', {'lessons' : lessons ,'year':year , 'user_profile': user_profile ,  'notifications' : notifications_count})


















# @login_required(login_url='register')
# def old_assignment_submit(request):
#     if request.method == 'POST':
#         assignment_id = request.POST['assignment']
#         assignment = Assignment.objects.get(assignment_id=assignment_id)



#         question1 = request.POST['question1']
#         question2 = request.POST['question2']
#         question3 = request.POST['question3']
#         question4 = request.POST['question4']
#         question5 = request.POST['question5']

        
        






#         if Question.objects.filter(assignment_id=assignment.assignment_id , number='1').first():
#             basic_question1 = Question.objects.get(assignment_id=assignment.assignment_id , number='1')
#         else:
#             basic_question1 = ''

#         if Question.objects.filter(assignment_id=assignment.assignment_id , number='2').first():
#             basic_question2 = Question.objects.get(assignment_id=assignment.assignment_id , number='2')
#         else:
#             basic_question2 = ''

#         if Question.objects.filter(assignment_id=assignment.assignment_id , number='3').first():
#             basic_question3 = Question.objects.get(assignment_id=assignment.assignment_id , number='3')
#         else:
#             basic_question3 = ''
        
#         if Question.objects.filter(assignment_id=assignment.assignment_id , number='4').first():
#             basic_question4 = Question.objects.get(assignment_id=assignment.assignment_id , number='4')
#         else:
#             basic_question4 = ''
        
#         if Question.objects.filter(assignment_id=assignment.assignment_id , number='5').first():
#             basic_question5 = Question.objects.get(assignment_id=assignment.assignment_id , number='5')
#         else:
#             basic_question5 = ''




#         if question1 == basic_question1.true:
#             student_answer1 = True
#             save_answer1 = Answer.objects.create(username=request.user.username, assignment_id=assignment.assignment_id , answer=question1 , true=True , question_id=basic_question1.question_id)
#         else:
#             student_answer1 = False
#             save_answer1 = Answer.objects.create(username=request.user.username, assignment_id=assignment.assignment_id , answer=question1 , true=False , question_id=basic_question1.question_id)



#         if question2 == basic_question2.true:
#             student_answer2 = True
#             save_answer2 = Answer.objects.create(username=request.user.username, assignment_id=assignment.assignment_id , answer=question2 , true=True , question_id=basic_question2.question_id)
#         else:
#             student_answer2 = False
#             save_answer2 = Answer.objects.create(username=request.user.username, assignment_id=assignment.assignment_id , answer=question2 , true=False ,question_id=basic_question2.question_id )



#         if question3 == basic_question3.true:
#             student_answer3 = True
#             save_answer3 = Answer.objects.create(username=request.user.username, assignment_id=assignment.assignment_id , answer=question3 , true=True , question_id=basic_question3.question_id)
#         else:
#             student_answer3 = False
#             save_answer3 = Answer.objects.create(username=request.user.username, assignment_id=assignment.assignment_id , answer=question3 , true=False ,question_id=basic_question3.question_id )



#         if question4 == basic_question4.true:
#             student_answer4 = True
#             save_answer4 = Answer.objects.create(username=request.user.username, assignment_id=assignment.assignment_id , answer=question4 , true=True , question_id=basic_question4.question_id)
#         else:
#             student_answer4 = False
#             save_answer4 = Answer.objects.create(username=request.user.username, assignment_id=assignment.assignment_id , answer=question4 , true=False ,question_id=basic_question4.question_id )
        


#         if question5 == basic_question5.true:
#             student_answer5 = True
#             save_answer5 = Answer.objects.create(username=request.user.username, assignment_id=assignment.assignment_id , answer=question5 , true=True , question_id=basic_question5.question_id)
#         else:
#             student_answer5 = False
#             save_answer5 = Answer.objects.create(username=request.user.username, assignment_id=assignment.assignment_id , answer=question5 , true=False ,question_id=basic_question5.question_id )



#         assignment_questions_count = Question.objects.filter(assignment_id=assignment.assignment_id).count()
#         submit_assignment = AssignmentSubmit.objects.create(username=request.user.username, assignment_id=assignment.assignment_id , answer1=student_answer1 , answer2=student_answer2 , answer3= student_answer3 , answer4=student_answer4 , answer5=student_answer5 , assignment_name=assignment.assignment_name , questions_count=assignment_questions_count)
#         submit_assignment.save()





#         return redirect('/assignment/progress/' + assignment_id)
#     else:
#         return redirect('/assignment/progress/' + assignment_id)


# @login_required(login_url='register')
# def old_submit_assignment(request):
#     if request.method == 'POST':
#         assignment_id = request.POST['assignment-id']
#         assignment = Assignment.objects.get(assignment_id=assignment_id)

#         for x in range(51):
#             if Question.objects.filter(assignment_id=assignment.assignment_id , number=x).first():
#                 question = Question.objects.get(assignment_id=assignment.assignment_id , number=x)
#                 answer = request.POST['answer-' + x]
#                 if answer == question.true:
#                     student_answer = True
#                     save_answer = Answer.objects.create(number=x , question_id=question.question_id , answer=answer , question=question.question , question_true=question.true , answer1=question.answer1 , answer2=question.answer2 , answer3=question.answer3 , answer4=question.answer4 , username=request.user.username, assignment_id=assignment.assignment_id , true=True )
#                 else:
#                     student_answer = False
#                     save_answer = Answer.objects.create(number=x , question_id=question.question_id , answer=answer , question=question.question , question_true=question.true , answer1=question.answer1 , answer2=question.answer2 , answer3=question.answer3 , answer4=question.answer4 , username=request.user.username, assignment_id=assignment.assignment_id , true=False )
#             else:
#                 student_answer = False

#         if Question.objects.filter(assignment_id=assignment.assignment_id , number='1').first():
#             question1 = Question.objects.get(assignment_id=assignment.assignment_id , number='1')
#             answer1 = request.POST['answer-1']
#             if answer1 == question1.true:
#                 student_answer1 = True
#                 save_answer1 = Answer.objects.create(number='1' , question_id=question1.question_id , answer=answer1 , question=question1.question , question_true=question1.true , answer1=question1.answer1 , answer2=question1.answer2 , answer3=question1.answer3 , answer4=question1.answer4 , username=request.user.username, assignment_id=assignment.assignment_id , true=True )
#             else:
#                 student_answer1 = False
#                 save_answer1 = Answer.objects.create(number='1' , question_id=question1.question_id , answer=answer1 , question=question1.question , question_true=question1.true , answer1=question1.answer1 , answer2=question1.answer2 , answer3=question1.answer3 , answer4=question1.answer4 , username=request.user.username, assignment_id=assignment.assignment_id , true=False )
#         else:
#             student_answer1 = False



#         if Question.objects.filter(assignment_id=assignment.assignment_id , number='2').first():
#             question2 = Question.objects.get(assignment_id=assignment.assignment_id , number='2')
#             answer2 = request.POST['answer-2']
#             if answer2 == question2.true:
#                 student_answer2 = True
#                 save_answer2 = Answer.objects.create(number='2' , question_id=question2.question_id , answer=answer2 , question=question2.question , question_true=question2.true , answer1=question2.answer1 , answer2=question2.answer2 , answer3=question2.answer3 , answer4=question2.answer4 , username=request.user.username, assignment_id=assignment.assignment_id , true=True )
#             else:
#                 student_answer2 = False
#                 save_answer2 = Answer.objects.create(number='2' , question_id=question2.question_id , answer=answer2 , question=question2.question , question_true=question2.true , answer1=question2.answer1 , answer2=question2.answer2 , answer3=question2.answer3 , answer4=question2.answer4 , username=request.user.username, assignment_id=assignment.assignment_id , true=False )
#         else:
#             student_answer2 = False




#         if Question.objects.filter(assignment_id=assignment.assignment_id , number='3').first():
#             question3 = Question.objects.get(assignment_id=assignment.assignment_id , number='3')
#             answer3 = request.POST['answer-3']
#             if answer3 == question3.true:
#                 student_answer3 = True
#                 save_answer3 = Answer.objects.create(number='3' , question_id=question3.question_id , answer=answer3 , question=question3.question , question_true=question3.true , answer1=question3.answer1 , answer2=question3.answer2 , answer3=question3.answer3 , answer4=question3.answer4 , username=request.user.username, assignment_id=assignment.assignment_id , true=True )
#             else:
#                 student_answer3 = False
#                 save_answer3 = Answer.objects.create(number='3' , question_id=question3.question_id , answer=answer3  , question=question3.question , question_true=question3.true , answer1=question3.answer1 , answer2=question3.answer2 , answer3=question3.answer3 , answer4=question3.answer4 , username=request.user.username, assignment_id=assignment.assignment_id , true= False )
#         else:
#             student_answer3 = False




#         if Question.objects.filter(assignment_id=assignment.assignment_id , number='4').first():
#             question4 = Question.objects.get(assignment_id=assignment.assignment_id , number='4')
#             answer4 = request.POST['answer-4']
#             if answer4 == question4.true:
#                 student_answer4 = True
#                 save_answer4 = Answer.objects.create(number='4' , question_id=question4.question_id , answer=answer4  , username=request.user.username, assignment_id=assignment.assignment_id , true=True )
#             else:
#                 student_answer4 = False
#                 save_answer4 = Answer.objects.create(number='4' , question_id=question4.question_id , answer=answer4  , username=request.user.username, assignment_id=assignment.assignment_id , true=False )
#         else:
#             student_answer4 = False

#         if Question.objects.filter(assignment_id=assignment.assignment_id , number='5').first():
#             question5 = Question.objects.get(assignment_id=assignment.assignment_id , number='5')
#             answer5 = request.POST['answer-5']
#             if answer5 == question5.true:
#                 student_answer5 = True
#                 save_answer5 = Answer.objects.create(number='5' , question_id=question5.question_id , answer=answer5  , username=request.user.username, assignment_id=assignment.assignment_id , true=True )
#             else:
#                 student_answer5 = False
#                 save_answer5 = Answer.objects.create(number='5' , question_id=question5.question_id , answer=answer5  , username=request.user.username, assignment_id=assignment.assignment_id , true=False )
#         else:
#             student_answer5 = False

#         if Question.objects.filter(assignment_id=assignment.assignment_id , number='6').first():
#             question6 = Question.objects.get(assignment_id=assignment.assignment_id , number='6')
#             answer6 = request.POST['answer-6']
#             if answer6 == question6.true:
#                 student_answer6 = True
#                 save_answer6 = Answer.objects.create(number='6' , question_id=question6.question_id , answer=answer6  , username=request.user.username, assignment_id=assignment.assignment_id , true=True )
#             else:
#                 student_answer6 = False
#                 save_answer6 = Answer.objects.create(number='6' , question_id=question6.question_id , answer=answer6  , username=request.user.username, assignment_id=assignment.assignment_id , true=False )
#         else:
#             student_answer6 = False

#         if Question.objects.filter(assignment_id=assignment.assignment_id , number='7').first():
#             question7 = Question.objects.get(assignment_id=assignment.assignment_id , number='7')
#             answer7 = request.POST['answer-7']
#             if answer7 == question7.true:
#                 student_answer7 = True
#                 save_answer7 = Answer.objects.create(number='7' , question_id=question7.question_id , answer=answer7  , username=request.user.username, assignment_id=assignment.assignment_id , true=True )
#             else:
#                 student_answer7 = False
#                 save_answer7 = Answer.objects.create(number='7' , question_id=question7.question_id , answer=answer7  , username=request.user.username, assignment_id=assignment.assignment_id , true=False )
#         else:
#             student_answer7 = False

#         if Question.objects.filter(assignment_id=assignment.assignment_id , number='8').first():
#             question8 = Question.objects.get(assignment_id=assignment.assignment_id , number='8')
#             answer8 = request.POST['answer-8']
#             if answer8 == question8.true:
#                 student_answer8 = True
#                 save_answer8 = Answer.objects.create(number='8' , question_id=question8.question_id , answer=answer8  , username=request.user.username, assignment_id=assignment.assignment_id , true=True )
#             else:
#                 student_answer8 = False
#                 save_answer8 = Answer.objects.create(number='8' , question_id=question8.question_id , answer=answer8  , username=request.user.username, assignment_id=assignment.assignment_id , true=False )
#         else:
#             student_answer8 = False

#         if Question.objects.filter(assignment_id=assignment.assignment_id , number='9').first():
#             question9 = Question.objects.get(assignment_id=assignment.assignment_id , number='9')
#             answer9 = request.POST['answer-9']
#             if answer9 == question9.true:
#                 student_answer9 = True
#                 save_answer9 = Answer.objects.create(number='9' , question_id=question9.question_id , answer=answer9  , username=request.user.username, assignment_id=assignment.assignment_id , true=True )
#             else:
#                 student_answer9 = False
#                 save_answer9 = Answer.objects.create(number='9' , question_id=question9.question_id , answer=answer9  , username=request.user.username, assignment_id=assignment.assignment_id , true=False )
#         else:
#             student_answer9 = False

#         if Question.objects.filter(assignment_id=assignment.assignment_id , number='10').first():
#             question10 = Question.objects.get(assignment_id=assignment.assignment_id , number='10')
#             answer10 = request.POST['answer-10']
#             if answer10 == question10.true:
#                 student_answer10 = True
#                 save_answer10 = Answer.objects.create(number='10' , question_id=question10.question_id , answer=answer10  , username=request.user.username, assignment_id=assignment.assignment_id , true=True )
#             else:
#                 student_answer10 = False
#                 save_answer10 = Answer.objects.create(number='10' , question_id=question10.question_id , answer=answer10  , username=request.user.username, assignment_id=assignment.assignment_id , true=False )
#         else:
#             student_answer10 = False

#         if Question.objects.filter(assignment_id=assignment.assignment_id , number='11').first():
#             question11 = Question.objects.get(assignment_id=assignment.assignment_id , number='11')
#             answer11 = request.POST['answer-11']
#             if answer11 == question11.true:
#                 student_answer11 = True
#                 save_answer11 = Answer.objects.create(number='11' , question_id=question11.question_id , answer=answer11, username=request.user.username, assignment_id=assignment.assignment_id , true=True )
#             else:
#                 student_answer11 = False
#                 save_answer11 = Answer.objects.create(number='11' , question_id=question11.question_id , answer=answer11  , username=request.user.username, assignment_id=assignment.assignment_id , true=False )
#         else:
#             student_answer11 = False

#         if Question.objects.filter(assignment_id=assignment.assignment_id , number='12').first():
#             question12 = Question.objects.get(assignment_id=assignment.assignment_id , number='12')
#             answer12 = request.POST['answer-12']
#             if answer12 == question12.true:
#                 student_answer12 = True
#                 save_answer12 = Answer.objects.create(number='12' , question_id=question12.question_id , answer=answer12, username=request.user.username, assignment_id=assignment.assignment_id , true=True )
#             else:
#                 student_answer12 = False
#                 save_answer12 = Answer.objects.create(number='12' , question_id=question12.question_id , answer=answer12, username=request.user.username, assignment_id=assignment.assignment_id , true=False )
#         else:
#             student_answer12 = False

#         if Question.objects.filter(assignment_id=assignment.assignment_id , number='13').first():
#             question13 = Question.objects.get(assignment_id=assignment.assignment_id , number='13')
#             answer13 = request.POST['answer-13']
#             if answer13 == question13.true:
#                 student_answer13 = True
#                 save_answer13 = Answer.objects.create(number='13' , question_id=question13.question_id , answer=answer13, username=request.user.username, assignment_id=assignment.assignment_id , true=True )
#             else:
#                 student_answer13 = False
#                 save_answer13 = Answer.objects.create(number='13' , question_id=question13.question_id , answer=answer13, username=request.user.username, assignment_id=assignment.assignment_id , true=False )
#         else:
#             student_answer13 = False

#         if Question.objects.filter(assignment_id=assignment.assignment_id , number='14').first():
#             question14 = Question.objects.get(assignment_id=assignment.assignment_id , number='14')
#             answer14 = request.POST['answer-14']
#             if answer14 == question14.true:
#                 student_answer14 = True
#                 save_answer14 = Answer.objects.create(number='14' , question_id=question14.question_id , answer=answer14, username=request.user.username, assignment_id=assignment.assignment_id , true=True )
#             else:
#                 student_answer14 = False
#                 save_answer14 = Answer.objects.create(number='14' , question_id=question14.question_id , answer=answer14, username=request.user.username, assignment_id=assignment.assignment_id , true=False )
#         else:
#             student_answer14 = False

#         if Question.objects.filter(assignment_id=assignment.assignment_id , number='15').first():
#             question15 = Question.objects.get(assignment_id=assignment.assignment_id , number='15')
#             answer15 = request.POST['answer-15']
#             if answer15 == question15.true:
#                 student_answer15 = True
#                 save_answer15 = Answer.objects.create(number='15' , question_id=question15.question_id , answer=answer15, username=request.user.username, assignment_id=assignment.assignment_id , true=True )
#             else:
#                 student_answer15 = False
#                 save_answer15 = Answer.objects.create(number='15' , question_id=question15.question_id , answer=answer15, username=request.user.username, assignment_id=assignment.assignment_id , true=False )
#         else:
#             student_answer15 = False

#         if Question.objects.filter(assignment_id=assignment.assignment_id , number='16').first():
#             question16 = Question.objects.get(assignment_id=assignment.assignment_id , number='16')
#             answer16 = request.POST['answer-16']
#             if answer16 == question16.true:
#                 student_answer16 = True
#                 save_answer16 = Answer.objects.create(number='16' , question_id=question16.question_id , answer=answer16, username=request.user.username, assignment_id=assignment.assignment_id , true=True )
#             else:
#                 student_answer16 = False
#                 save_answer16 = Answer.objects.create(number='16' , question_id=question16.question_id , answer=answer16, username=request.user.username, assignment_id=assignment.assignment_id , true=False )
#         else:
#             student_answer = False

#         if Question.objects.filter(assignment_id=assignment.assignment_id , number='17').first():
#             question17 = Question.objects.get(assignment_id=assignment.assignment_id , number='17')
#             answer17 = request.POST['answer-17']
#             if answer17 == question17.true:
#                 student_answer17 = True
#                 save_answer17 = Answer.objects.create(number='17' , question_id=question17.question_id , answer=answer17, username=request.user.username, assignment_id=assignment.assignment_id , true=True )
#             else:
#                 student_answer17 = False
#                 save_answer17 = Answer.objects.create(number='17' , question_id=question17.question_id , answer=answer17, username=request.user.username, assignment_id=assignment.assignment_id , true=False )
#         else:
#             student_answer17 = False

#         if Question.objects.filter(assignment_id=assignment.assignment_id , number='18').first():
#             question18 = Question.objects.get(assignment_id=assignment.assignment_id , number='18')
#             answer18 = request.POST['answer-18']
#             if answer18 == question18.true:
#                 student_answer18 = True
#                 save_answer18 = Answer.objects.create(number='18' , question_id=question18.question_id , answer=answer18, username=request.user.username, assignment_id=assignment.assignment_id , true=True )
#             else:
#                 student_answer18 = False
#                 save_answer18 = Answer.objects.create(number='18' , question_id=question18.question_id , answer=answer18, username=request.user.username, assignment_id=assignment.assignment_id , true=False )
#         else:
#             student_answer18 = False

#         if Question.objects.filter(assignment_id=assignment.assignment_id , number='19').first():
#             question19 = Question.objects.get(assignment_id=assignment.assignment_id , number='19')
#             answer19 = request.POST['answer-19']
#             if answer19 == question19.true:
#                 student_answer19 = True
#                 save_answer19 = Answer.objects.create(number='19' , question_id=question19.question_id , answer=answer19, username=request.user.username, assignment_id=assignment.assignment_id , true=True )
#             else:
#                 student_answer19 = False
#                 save_answer19 = Answer.objects.create(number='19' , question_id=question19.question_id , answer=answer19, username=request.user.username, assignment_id=assignment.assignment_id , true=False )
#         else:
#             student_answer19 = False

#         if Question.objects.filter(assignment_id=assignment.assignment_id , number='20').first():
#             question20 = Question.objects.get(assignment_id=assignment.assignment_id , number='20')
#             answer20 = request.POST['answer-20']
#             if answer20 == question20.true:
#                 student_answer20 = True
#                 save_answer20 = Answer.objects.create(number='20' , question_id=question20.question_id , answer=answer20, username=request.user.username, assignment_id=assignment.assignment_id , true=True )
#             else:
#                 student_answer20 = False
#                 save_answer20 = Answer.objects.create(number='20' , question_id=question20.question_id , answer=answer20, username=request.user.username, assignment_id=assignment.assignment_id , true=False )
#         else:
#             student_answer20 = False

#         if Question.objects.filter(assignment_id=assignment.assignment_id , number='21').first():
#             question21 = Question.objects.get(assignment_id=assignment.assignment_id , number='21')


#         if Question.objects.filter(assignment_id=assignment.assignment_id , number='22').first():
#             question22 = Question.objects.get(assignment_id=assignment.assignment_id , number='22')


#         if Question.objects.filter(assignment_id=assignment.assignment_id , number='23').first():
#             question23 = Question.objects.get(assignment_id=assignment.assignment_id , number='23')


#         if Question.objects.filter(assignment_id=assignment.assignment_id , number='24').first():
#             question24 = Question.objects.get(assignment_id=assignment.assignment_id , number='24')


#         if Question.objects.filter(assignment_id=assignment.assignment_id , number='25').first():
#             question25 = Question.objects.get(assignment_id=assignment.assignment_id , number='25')


#         if Question.objects.filter(assignment_id=assignment.assignment_id , number='26').first():
#             question26 = Question.objects.get(assignment_id=assignment.assignment_id , number='26')


#         if Question.objects.filter(assignment_id=assignment.assignment_id , number='27').first():
#             question27 = Question.objects.get(assignment_id=assignment.assignment_id , number='27')


#         if Question.objects.filter(assignment_id=assignment.assignment_id , number='28').first():
#             question28 = Question.objects.get(assignment_id=assignment.assignment_id , number='28')


#         if Question.objects.filter(assignment_id=assignment.assignment_id , number='29').first():
#             question29 = Question.objects.get(assignment_id=assignment.assignment_id , number='29')


#         if Question.objects.filter(assignment_id=assignment.assignment_id , number='30').first():
#             question30 = Question.objects.get(assignment_id=assignment.assignment_id , number='30')


#         if Question.objects.filter(assignment_id=assignment.assignment_id , number='31').first():
#             question31 = Question.objects.get(assignment_id=assignment.assignment_id , number='31')


#         if Question.objects.filter(assignment_id=assignment.assignment_id , number='32').first():
#             question32 = Question.objects.get(assignment_id=assignment.assignment_id , number='32')


#         if Question.objects.filter(assignment_id=assignment.assignment_id , number='33').first():
#             question33 = Question.objects.get(assignment_id=assignment.assignment_id , number='33')


#         if Question.objects.filter(assignment_id=assignment.assignment_id , number='34').first():
#             question34 = Question.objects.get(assignment_id=assignment.assignment_id , number='34')


#         if Question.objects.filter(assignment_id=assignment.assignment_id , number='35').first():
#             question35 = Question.objects.get(assignment_id=assignment.assignment_id , number='35')


#         if Question.objects.filter(assignment_id=assignment.assignment_id , number='36').first():
#             question36 = Question.objects.get(assignment_id=assignment.assignment_id , number='36')


#         if Question.objects.filter(assignment_id=assignment.assignment_id , number='37').first():
#             question37 = Question.objects.get(assignment_id=assignment.assignment_id , number='37')


#         if Question.objects.filter(assignment_id=assignment.assignment_id , number='38').first():
#             question38 = Question.objects.get(assignment_id=assignment.assignment_id , number='38')


#         if Question.objects.filter(assignment_id=assignment.assignment_id , number='39').first():
#             question39 = Question.objects.get(assignment_id=assignment.assignment_id , number='39')


#         if Question.objects.filter(assignment_id=assignment.assignment_id , number='40').first():
#             question40 = Question.objects.get(assignment_id=assignment.assignment_id , number='40')


#         if Question.objects.filter(assignment_id=assignment.assignment_id , number='41').first():
#             question41 = Question.objects.get(assignment_id=assignment.assignment_id , number='41')


#         if Question.objects.filter(assignment_id=assignment.assignment_id , number='42').first():
#             question42 = Question.objects.get(assignment_id=assignment.assignment_id , number='42')


#         if Question.objects.filter(assignment_id=assignment.assignment_id , number='43').first():
#             question43 = Question.objects.get(assignment_id=assignment.assignment_id , number='43')


#         if Question.objects.filter(assignment_id=assignment.assignment_id , number='44').first():
#             question44 = Question.objects.get(assignment_id=assignment.assignment_id , number='44')


#         if Question.objects.filter(assignment_id=assignment.assignment_id , number='45').first():
#             question45 = Question.objects.get(assignment_id=assignment.assignment_id , number='45')


#         if Question.objects.filter(assignment_id=assignment.assignment_id , number='46').first():
#             question46 = Question.objects.get(assignment_id=assignment.assignment_id , number='46')


#         if Question.objects.filter(assignment_id=assignment.assignment_id , number='47').first():
#             question47 = Question.objects.get(assignment_id=assignment.assignment_id , number='47')


#         if Question.objects.filter(assignment_id=assignment.assignment_id , number='48').first():
#             question48 = Question.objects.get(assignment_id=assignment.assignment_id , number='48')


#         if Question.objects.filter(assignment_id=assignment.assignment_id , number='49').first():
#             question49 = Question.objects.get(assignment_id=assignment.assignment_id , number='49')


#         if Question.objects.filter(assignment_id=assignment.assignment_id , number='50').first():
#             question50 = Question.objects.get(assignment_id=assignment.assignment_id , number='50')





#         assignment_questions_count = assignment.questions_count
#         student_true_answers_count = Answer.objects.filter(true=True , assignment_id=assignment.assignment_id , username=request.user.username).count()
#         student_false_answers_count = Answer.objects.filter(true=False , assignment_id=assignment.assignment_id , username=request.user.username).count()






#         submit_assignment = AssignmentSubmit.objects.create( answer1=student_answer1 , answer2=student_answer2 , answer3= student_answer3 , answer4= student_answer4 , answer5= student_answer5 , answer6= student_answer6 , answer7= student_answer7 , answer8= student_answer8 , answer9= student_answer9 , answer10= student_answer10  , username=request.user.username, assignment_id=assignment.assignment_id  , assignment_name=assignment.assignment_name , questions_count=assignment_questions_count , true_answers=student_true_answers_count , false_answers=student_false_answers_count)
#         submit_assignment.save()



#         return redirect('/assignment/' + assignment_id)
    
#     else:
#         return redirect('/assignment/' + assignment_id)
    


# def old_assignment_progress(request , slug):
#     if User.objects.filter(username=request.user.username).first():
#         user_object = User.objects.get(username=request.user.username)
#         user_profile = Profile.objects.get(user=user_object)

#         notifications_count = Notification.objects.filter(username=request.user.username).count()
#     else:
#         user_profile = ''
#         notifications_count = ''


#     assignment = get_object_or_404(Assignment ,slug=slug)
#     questions = Question.objects.filter(assignment_id=assignment.assignment_id)

#     if assignment.post_id == 'none':
#         button_text = 'no'
#         lesson_text = ''
#         lesson = ''
#         post = ''
#     else:
#         if Post.objects.filter(id=assignment.post_id).first():

#             button_text = 'yes'
#             lesson = Post.objects.get(id=assignment.post_id)
#             post = Post.objects.get(id=assignment.post_id)

#             if BuyLesson.objects.filter(username=request.user.username, post_id=lesson.id).first():
#                 lesson_text = 'buyed'
#             else:
#                 if user_profile.instructor == False:
#                     lesson_text = 'not'
                    
#                 else:
#                     lesson_text = 'instructor'
#         else:
#             button_text = 'no'
#             lesson_text = ''
#             lesson = ''
#             post = ''



#     if AssignmentOpen.objects.filter(username=request.user.username, assignment_id=assignment.assignment_id).first():
#         if AssignmentSubmit.objects.filter(username=request.user.username, assignment_id=assignment.assignment_id).first():
#             if user_profile.instructor == False:
#                 text = 'submited'
#             else:
#                 text = 'instructor'
#         else:
#             if user_profile.instructor == False:
#                 text = 'complete'
#             else:
#                 text = 'instructor'
#     else:
#         if user_profile.instructor == False:
#             text = 'start'
#         else:
#             text = 'instructor'






#     if AssignmentSubmit.objects.filter(username=request.user.username, assignment_id=assignment.assignment_id).first():
#         if Question.objects.filter(assignment_id=assignment.assignment_id , number='1').first():
#             question1 = Question.objects.get(assignment_id=assignment.assignment_id , number='1')
#             user_answer1 = Answer.objects.get(question_id=question1.question_id , assignment_id=assignment.assignment_id , username=request.user.username)
#         else:
#             user_answer1 = ''
#             question1 = ''
            

#         if Question.objects.filter(assignment_id=assignment.assignment_id , number='2').first():
#             question2 = Question.objects.get(assignment_id=assignment.assignment_id , number='2')
#             user_answer2 = Answer.objects.get(question_id=question2.question_id , assignment_id=assignment.assignment_id , username=request.user.username)
#         else:
#             user_answer2 = ''
#             question2 = ''

#         if Question.objects.filter(assignment_id=assignment.assignment_id , number='3').first():
#             question3 = Question.objects.get(assignment_id=assignment.assignment_id , number='3')
#             user_answer3 = Answer.objects.get(question_id=question3.question_id , assignment_id=assignment.assignment_id , username=request.user.username)
#         else:
#             user_answer3 = ''
#             question3 = ''

#         if Question.objects.filter(assignment_id=assignment.assignment_id , number='4').first():
#             question4 = Question.objects.get(assignment_id=assignment.assignment_id , number='4')
#             user_answer4 = Answer.objects.get(question_id=question4.question_id , assignment_id=assignment.assignment_id , username=request.user.username)
#         else:
#             user_answer4 = ''
#             question4 = ''

#         if Question.objects.filter(assignment_id=assignment.assignment_id , number='5').first():
#             question5 = Question.objects.get(assignment_id=assignment.assignment_id , number='5')
#             user_answer5 = Answer.objects.get(question_id=question5.question_id , assignment_id=assignment.assignment_id , username=request.user.username)
#         else:
#             user_answer5 = ''
#             question5 = ''

#         if Question.objects.filter(assignment_id=assignment.assignment_id , number='6').first():
#             question6 = Question.objects.get(assignment_id=assignment.assignment_id , number='6')
#             user_answer6 = Answer.objects.get(question_id=question6.question_id , assignment_id=assignment.assignment_id , username=request.user.username)
#         else:
#             user_answer6 = ''
#             question6 = ''

#         if Question.objects.filter(assignment_id=assignment.assignment_id , number='7').first():
#             question7 = Question.objects.get(assignment_id=assignment.assignment_id , number='7')
#             user_answer7 = Answer.objects.get(question_id=question7.question_id , assignment_id=assignment.assignment_id , username=request.user.username)
#         else:
#             user_answer7 = ''
#             question7 = ''

#         if Question.objects.filter(assignment_id=assignment.assignment_id , number='8').first():
#             question8 = Question.objects.get(assignment_id=assignment.assignment_id , number='8')
#             user_answer8 = Answer.objects.get(question_id=question8.question_id , assignment_id=assignment.assignment_id , username=request.user.username)
#         else:
#             user_answer8 = ''
#             questio8 = ''

#         if Question.objects.filter(assignment_id=assignment.assignment_id , number='9').first():
#             question9 = Question.objects.get(assignment_id=assignment.assignment_id , number='9')
#             user_answer9 = Answer.objects.get(question_id=question9.question_id , assignment_id=assignment.assignment_id , username=request.user.username)
#         else:
#             user_answer9 = ''
#             question9 = ''

#         if Question.objects.filter(assignment_id=assignment.assignment_id , number='10').first():
#             question10 = Question.objects.get(assignment_id=assignment.assignment_id , number='10')
#             user_answer10 = Answer.objects.get(question_id=question10.question_id , assignment_id=assignment.assignment_id , username=request.user.username)
#         else:
#             user_answer10 = ''
#             question10 = ''

#         if Question.objects.filter(assignment_id=assignment.assignment_id , number='11').first():
#             question11 = Question.objects.get(assignment_id=assignment.assignment_id , number='11')
#             user_answer11 = Answer.objects.get(question_id=question11.question_id , assignment_id=assignment.assignment_id , username=request.user.username)
#         else:
#             user_answer11 = ''
#             question11 = ''

#         if Question.objects.filter(assignment_id=assignment.assignment_id , number='12').first():
#             question12 = Question.objects.get(assignment_id=assignment.assignment_id , number='12')
#             user_answer12 = Answer.objects.get(question_id=question12.question_id , assignment_id=assignment.assignment_id , username=request.user.username)
#         else:
#             user_answer12 = ''
#             question12 = ''

#         if Question.objects.filter(assignment_id=assignment.assignment_id , number='13').first():
#             question13 = Question.objects.get(assignment_id=assignment.assignment_id , number='13')
#             user_answer13 = Answer.objects.get(question_id=question13.question_id , assignment_id=assignment.assignment_id , username=request.user.username)
#         else:
#             user_answer13 = ''
#             question13 = ''

#         if Question.objects.filter(assignment_id=assignment.assignment_id , number='14').first():
#             question14 = Question.objects.get(assignment_id=assignment.assignment_id , number='14')
#             user_answer14 = Answer.objects.get(question_id=question14.question_id , assignment_id=assignment.assignment_id , username=request.user.username)
#         else:
#             user_answer14 = ''
#             question14 = ''

#         if Question.objects.filter(assignment_id=assignment.assignment_id , number='15').first():
#             question15 = Question.objects.get(assignment_id=assignment.assignment_id , number='15')
#             user_answer15 = Answer.objects.get(question_id=question15.question_id , assignment_id=assignment.assignment_id , username=request.user.username)
#         else:
#             user_answer15 = ''
#             question15 = ''

#         if Question.objects.filter(assignment_id=assignment.assignment_id , number='16').first():
#             question16 = Question.objects.get(assignment_id=assignment.assignment_id , number='16')
#             user_answer16 = Answer.objects.get(question_id=question16.question_id , assignment_id=assignment.assignment_id , username=request.user.username)
#         else:
#             user_answer16 = ''
#             question16 = ''

#         if Question.objects.filter(assignment_id=assignment.assignment_id , number='17').first():
#             question17 = Question.objects.get(assignment_id=assignment.assignment_id , number='17')
#             user_answer17 = Answer.objects.get(question_id=question17.question_id , assignment_id=assignment.assignment_id , username=request.user.username)
#         else:
#             user_answer17 = ''
#             question17 = ''

#         if Question.objects.filter(assignment_id=assignment.assignment_id , number='18').first():
#             question18 = Question.objects.get(assignment_id=assignment.assignment_id , number='18')
#             user_answer18 = Answer.objects.get(question_id=question18.question_id , assignment_id=assignment.assignment_id , username=request.user.username)
#         else:
#             user_answer18 = ''
#             question18 = ''

#         if Question.objects.filter(assignment_id=assignment.assignment_id , number='19').first():
#             question19 = Question.objects.get(assignment_id=assignment.assignment_id , number='19')
#             user_answer19 = Answer.objects.get(question_id=question19.question_id , assignment_id=assignment.assignment_id , username=request.user.username)
#         else:
#             user_answer19 = ''
#             question19 = ''

#         if Question.objects.filter(assignment_id=assignment.assignment_id , number='20').first():
#             question20 = Question.objects.get(assignment_id=assignment.assignment_id , number='20')
#             user_answer20 = Answer.objects.get(question_id=question20.question_id , assignment_id=assignment.assignment_id , username=request.user.username)
#         else:
#             user_answer20 = ''
#             question20 = ''

#         if Question.objects.filter(assignment_id=assignment.assignment_id , number='21').first():
#             question21 = Question.objects.get(assignment_id=assignment.assignment_id , number='21')
#             user_answer21 = Answer.objects.get(question_id=question21.question_id , assignment_id=assignment.assignment_id , username=request.user.username)
#         else:
#             user_answer21 = ''
#             question21 = ''

#         if Question.objects.filter(assignment_id=assignment.assignment_id , number='22').first():
#             question22 = Question.objects.get(assignment_id=assignment.assignment_id , number='22')
#             user_answer22 = Answer.objects.get(question_id=question22.question_id , assignment_id=assignment.assignment_id , username=request.user.username)
#         else:
#             user_answer22 = ''
#             question22 = ''

#         if Question.objects.filter(assignment_id=assignment.assignment_id , number='23').first():
#             question23 = Question.objects.get(assignment_id=assignment.assignment_id , number='23')
#             user_answer23 = Answer.objects.get(question_id=question23.question_id , assignment_id=assignment.assignment_id , username=request.user.username)
#         else:
#             user_answer23 = ''
#             question23 = ''

#         if Question.objects.filter(assignment_id=assignment.assignment_id , number='24').first():
#             question24 = Question.objects.get(assignment_id=assignment.assignment_id , number='24')
#             user_answer24 = Answer.objects.get(question_id=question24.question_id , assignment_id=assignment.assignment_id , username=request.user.username)
#         else:
#             user_answer24 = ''
#             question24 = ''

#         if Question.objects.filter(assignment_id=assignment.assignment_id , number='25').first():
#             question25 = Question.objects.get(assignment_id=assignment.assignment_id , number='25')
#             user_answer25 = Answer.objects.get(question_id=question25.question_id , assignment_id=assignment.assignment_id , username=request.user.username)
#         else:
#             user_answer25 = ''
#             question25 = ''

#         if Question.objects.filter(assignment_id=assignment.assignment_id , number='26').first():
#             question26 = Question.objects.get(assignment_id=assignment.assignment_id , number='26')
#             user_answer26 = Answer.objects.get(question_id=question26.question_id , assignment_id=assignment.assignment_id , username=request.user.username)
#         else:
#             user_answer26 = ''
#             question26 = ''

#         if Question.objects.filter(assignment_id=assignment.assignment_id , number='27').first():
#             question27 = Question.objects.get(assignment_id=assignment.assignment_id , number='27')
#             user_answer27 = Answer.objects.get(question_id=question27.question_id , assignment_id=assignment.assignment_id , username=request.user.username)
#         else:
#             user_answer27 = ''
#             question27 = ''

#         if Question.objects.filter(assignment_id=assignment.assignment_id , number='28').first():
#             question28 = Question.objects.get(assignment_id=assignment.assignment_id , number='28')
#             user_answer28 = Answer.objects.get(question_id=question28.question_id , assignment_id=assignment.assignment_id , username=request.user.username)
#         else:
#             user_answer28 = ''
#             question28 = ''

#         if Question.objects.filter(assignment_id=assignment.assignment_id , number='29').first():
#             question29 = Question.objects.get(assignment_id=assignment.assignment_id , number='29')
#             user_answer29 = Answer.objects.get(question_id=question29.question_id , assignment_id=assignment.assignment_id , username=request.user.username)
#         else:
#             user_answer29 = ''
#             question29 = ''

#         if Question.objects.filter(assignment_id=assignment.assignment_id , number='30').first():
#             question30 = Question.objects.get(assignment_id=assignment.assignment_id , number='30')
#             user_answer30 = Answer.objects.get(question_id=question30.question_id , assignment_id=assignment.assignment_id , username=request.user.username)
#         else:
#             user_answer30 = ''
#             question30 = ''

#         if Question.objects.filter(assignment_id=assignment.assignment_id , number='31').first():
#             question31 = Question.objects.get(assignment_id=assignment.assignment_id , number='31')
#             user_answer31 = Answer.objects.get(question_id=question31.question_id , assignment_id=assignment.assignment_id , username=request.user.username)
#         else:
#             user_answer31 = ''
#             question31 = ''

#         if Question.objects.filter(assignment_id=assignment.assignment_id , number='32').first():
#             question32 = Question.objects.get(assignment_id=assignment.assignment_id , number='32')
#             user_answer32 = Answer.objects.get(question_id=question32.question_id , assignment_id=assignment.assignment_id , username=request.user.username)
#         else:
#             user_answer32 = ''
#             question32 = ''

#         if Question.objects.filter(assignment_id=assignment.assignment_id , number='33').first():
#             question33 = Question.objects.get(assignment_id=assignment.assignment_id , number='33')
#             user_answer33 = Answer.objects.get(question_id=question33.question_id , assignment_id=assignment.assignment_id , username=request.user.username)
#         else:
#             user_answer33 = ''
#             question33 = ''

#         if Question.objects.filter(assignment_id=assignment.assignment_id , number='34').first():
#             question34 = Question.objects.get(assignment_id=assignment.assignment_id , number='34')
#             user_answer34 = Answer.objects.get(question_id=question34.question_id , assignment_id=assignment.assignment_id , username=request.user.username)
#         else:
#             user_answer34 = ''
#             question34 = ''

#         if Question.objects.filter(assignment_id=assignment.assignment_id , number='35').first():
#             question35 = Question.objects.get(assignment_id=assignment.assignment_id , number='35')
#             user_answer35 = Answer.objects.get(question_id=question35.question_id , assignment_id=assignment.assignment_id , username=request.user.username)
#         else:
#             user_answer35 = ''
#             question35 = ''

#         if Question.objects.filter(assignment_id=assignment.assignment_id , number='36').first():
#             question36 = Question.objects.get(assignment_id=assignment.assignment_id , number='36')
#             user_answer36 = Answer.objects.get(question_id=question36.question_id , assignment_id=assignment.assignment_id , username=request.user.username)
#         else:
#             user_answer36 = ''
#             question36 = ''

#         if Question.objects.filter(assignment_id=assignment.assignment_id , number='37').first():
#             question37 = Question.objects.get(assignment_id=assignment.assignment_id , number='37')
#             user_answer37 = Answer.objects.get(question_id=question37.question_id , assignment_id=assignment.assignment_id , username=request.user.username)
#         else:
#             user_answer37 = ''
#             question37 = ''

#         if Question.objects.filter(assignment_id=assignment.assignment_id , number='38').first():
#             question38 = Question.objects.get(assignment_id=assignment.assignment_id , number='38')
#             user_answer38 = Answer.objects.get(question_id=question38.question_id , assignment_id=assignment.assignment_id , username=request.user.username)
#         else:
#             user_answer38 = ''
#             question38 = ''

#         if Question.objects.filter(assignment_id=assignment.assignment_id , number='39').first():
#             question39 = Question.objects.get(assignment_id=assignment.assignment_id , number='39')
#             user_answer39 = Answer.objects.get(question_id=question39.question_id , assignment_id=assignment.assignment_id , username=request.user.username)
#         else:
#             user_answer39 = ''
#             question39 = ''

#         if Question.objects.filter(assignment_id=assignment.assignment_id , number='40').first():
#             question40 = Question.objects.get(assignment_id=assignment.assignment_id , number='40')
#             user_answer40 = Answer.objects.get(question_id=question40.question_id , assignment_id=assignment.assignment_id , username=request.user.username)
#         else:
#             user_answer40 = ''
#             question40 = ''

#         if Question.objects.filter(assignment_id=assignment.assignment_id , number='41').first():
#             question41 = Question.objects.get(assignment_id=assignment.assignment_id , number='41')
#             user_answer41 = Answer.objects.get(question_id=question41.question_id , assignment_id=assignment.assignment_id , username=request.user.username)
#         else:
#             user_answer41 = ''
#             question41 = ''

#         if Question.objects.filter(assignment_id=assignment.assignment_id , number='42').first():
#             question42 = Question.objects.get(assignment_id=assignment.assignment_id , number='42')
#             user_answer42 = Answer.objects.get(question_id=question42.question_id , assignment_id=assignment.assignment_id , username=request.user.username)
#         else:
#             user_answer42 = ''
#             question42 = ''

#         if Question.objects.filter(assignment_id=assignment.assignment_id , number='43').first():
#             question43 = Question.objects.get(assignment_id=assignment.assignment_id , number='43')
#             user_answer43 = Answer.objects.get(question_id=question43.question_id , assignment_id=assignment.assignment_id , username=request.user.username)
#         else:
#             user_answer43 = ''
#             question43 = ''

#         if Question.objects.filter(assignment_id=assignment.assignment_id , number='44').first():
#             question44 = Question.objects.get(assignment_id=assignment.assignment_id , number='44')
#             user_answer44 = Answer.objects.get(question_id=question44.question_id , assignment_id=assignment.assignment_id , username=request.user.username)
#         else:
#             user_answer44 = ''
#             question44 = ''

#         if Question.objects.filter(assignment_id=assignment.assignment_id , number='45').first():
#             question45 = Question.objects.get(assignment_id=assignment.assignment_id , number='45')
#             user_answer45 = Answer.objects.get(question_id=question45.question_id , assignment_id=assignment.assignment_id , username=request.user.username)
#         else:
#             user_answer45 = ''
#             question45 = ''

#         if Question.objects.filter(assignment_id=assignment.assignment_id , number='46').first():
#             question46 = Question.objects.get(assignment_id=assignment.assignment_id , number='46')
#             user_answer46 = Answer.objects.get(question_id=question46.question_id , assignment_id=assignment.assignment_id , username=request.user.username)
#         else:
#             user_answer46 = ''
#             question46 = ''

#         if Question.objects.filter(assignment_id=assignment.assignment_id , number='47').first():
#             question47 = Question.objects.get(assignment_id=assignment.assignment_id , number='47')
#             user_answer47 = Answer.objects.get(question_id=question47.question_id , assignment_id=assignment.assignment_id , username=request.user.username)
#         else:
#             user_answer47 = ''
#             question47 = ''

#         if Question.objects.filter(assignment_id=assignment.assignment_id , number='48').first():
#             question48 = Question.objects.get(assignment_id=assignment.assignment_id , number='48')
#             user_answer48 = Answer.objects.get(question_id=question48.question_id , assignment_id=assignment.assignment_id , username=request.user.username)
#         else:
#             user_answer48 = ''
#             question48 = ''

#         if Question.objects.filter(assignment_id=assignment.assignment_id , number='49').first():
#             question49 = Question.objects.get(assignment_id=assignment.assignment_id , number='49')
#             user_answer49 = Answer.objects.get(question_id=question49.question_id , assignment_id=assignment.assignment_id , username=request.user.username)
#         else:
#             user_answer49 = ''
#             question49 = ''

#         if Question.objects.filter(assignment_id=assignment.assignment_id , number='50').first():
#             question50 = Question.objects.get(assignment_id=assignment.assignment_id , number='50')
#             user_answer50 = Answer.objects.get(question_id=question50.question_id , assignment_id=assignment.assignment_id , username=request.user.username)
#         else:
#             user_answer50= ''
#             question50 = ''



#         user_submit = AssignmentSubmit.objects.get(assignment_id=assignment.assignment_id , username=request.user.username)
#         results = Answer.objects.filter(assignment_id=assignment.assignment_id , username=request.user.username)


#         context =  {

#         'user_profile': user_profile,

#         'text' : text  , 
#         'button_text' : button_text , 
#         'lesson_text':lesson_text ,
#         'post' : post,

#         'notifications' : notifications_count , 
#         'assignment' : assignment , 
#         'results' : results ,


#         'question1' : question1 ,
#         'question2' : question2 ,
#         'question3' : question3 ,




#         'user_submit' : user_submit ,


#         'user_answer1' : user_answer1 ,
#         'user_answer2' : user_answer2 ,
#         'user_answer3' : user_answer3 ,
#         'user_answer4' : user_answer4 ,
#         'user_answer5' : user_answer5 ,
#         'user_answer6' : user_answer6 ,
#         'user_answer7' : user_answer7 ,
#         'user_answer8' : user_answer8 ,
#         'user_answer9' : user_answer9 ,
#         'user_answer10' : user_answer10 ,
#         'user_answer11' : user_answer11 ,
#         'user_answer12' : user_answer12 ,
#         'user_answer13' : user_answer13 ,
#         'user_answer14' : user_answer14 ,
#         'user_answer15' : user_answer15 ,
#         'user_answer16' : user_answer16 ,
#         'user_answer17' : user_answer17 ,
#         'user_answer18' : user_answer18 ,
#         'user_answer19' : user_answer19 ,
#         'user_answer20' : user_answer20 ,
#         'user_answer21' : user_answer21 ,
#         'user_answer22' : user_answer22 ,
#         'user_answer23' : user_answer23 ,
#         'user_answer24' : user_answer24 ,
#         'user_answer25' : user_answer25 ,
#         'user_answer26' : user_answer26 ,
#         'user_answer27' : user_answer27,
#         'user_answer28' : user_answer28 ,
#         'user_answer29' : user_answer29 ,
#         'user_answer30' : user_answer30 ,
#         'user_answer31' : user_answer31 ,
#         'user_answer32' : user_answer32 ,
#         'user_answer33' : user_answer33 ,
#         'user_answer34' : user_answer34 ,
#         'user_answer35' : user_answer35 ,
#         'user_answer36' : user_answer36 ,
#         'user_answer37' : user_answer37 ,
#         'user_answer38' : user_answer38 ,
#         'user_answer39' : user_answer39 ,
#         'user_answer40' : user_answer40 ,
#         'user_answer41' : user_answer41 ,
#         'user_answer42' : user_answer42 ,
#         'user_answer43' : user_answer43 ,
#         'user_answer44' : user_answer44 ,
#         'user_answer45' : user_answer45 ,
#         'user_answer46' : user_answer46 ,
#         'user_answer47' : user_answer47 ,
#         'user_answer48' : user_answer48 ,
#         'user_answer49' : user_answer49 ,
#         'user_answer50' : user_answer50 ,
#         }

#     else:
#         context =  {
#         'user_profile': user_profile,
#         'text' : text  , 
#         'button_text' : button_text , 
#         'lesson_text':lesson_text ,
#         'post' : post,
#         'notifications' : notifications_count , 
#         'assignment' : assignment , 

#         'questions' : questions ,
#     }





#     return render(request, 'assignment/assignment-progress.html', context)





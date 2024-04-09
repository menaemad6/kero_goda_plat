from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from core.models import Notification ,  Activity , Reply , Comment, Code , RechargeRequest, Profile, Post, LikePost, FollowersCount , Subject , GetPremium , News , Instructor , BuyLesson
from itertools import chain
import random

from core.models import Assignment , AssignmentOpen , Question , AssignmentSubmit , Answer , Part


from django.shortcuts import get_object_or_404

# Create your views here.


# Teacher Functions 

@login_required(login_url='register')
def dashboard_assignments(request):
    if User.objects.filter(username=request.user.username).first():
        user_object = User.objects.get(username=request.user.username)
        user_profile = Profile.objects.get(user=user_object)

        notifications_count = Notification.objects.filter(username=request.user.username).count()
    else:
        user_profile = ''
        notifications_count = ''

    assignments = Assignment.objects.filter(username=request.user.username)
    teacher_posts = Post.objects.filter(user=request.user.username)

    if Assignment.objects.filter(username=request.user.username).first():
        for assignment in assignments:
            if Question.objects.filter(assignment_id=assignment.assignment_id).first():
                questions_count = Question.objects.filter(assignment_id=assignment.assignment_id).count()
            else:
                questions_count = ''
    else:
        questions_count = ''



    return render(request, 'dark/assignments.html', {'user_profile': user_profile , 'notifications' : notifications_count , 'assignments' : assignments , 'posts':teacher_posts , 'questions_count' : questions_count})

@login_required(login_url='register')
def dashboard_assignment_detail(request , slug):
    if User.objects.filter(username=request.user.username).first():
        user_object = User.objects.get(username=request.user.username)
        user_profile = Profile.objects.get(user=user_object)

        notifications_count = Notification.objects.filter(username=request.user.username).count()
    else:
        user_profile = ''
        notifications_count = ''


    assignment = get_object_or_404(Assignment ,slug=slug)
    questions = Question.objects.filter(assignment_id=assignment.assignment_id)

    questions_count = questions.count()



    return render(request, 'dashboard/assignment-detail.html', {'assignment' : assignment , 'questions' : questions , 'questions_count':questions_count , 'user_profile': user_profile,  'notifications' : notifications_count })



@login_required(login_url='register')
def assignment_applicants(request , slug):
    if User.objects.filter(username=request.user.username).first():
        user_object = User.objects.get(username=request.user.username)
        user_profile = Profile.objects.get(user=user_object)

        notifications_count = Notification.objects.filter(username=request.user.username).count()
    else:
        user_profile = ''
        notifications_count = ''

    assignment = get_object_or_404(Assignment ,slug=slug)
    no_of_questions = Question.objects.filter(assignment_id=assignment.assignment_id).count()

    applicants = AssignmentSubmit.objects.filter(assignment_id=assignment.assignment_id)

    return render(request, 'dark/applicants.html', {'user_profile': user_profile , 'notifications' : notifications_count , 'assignment' : assignment , 'applicants' : applicants , 'questions_count':no_of_questions})

@login_required(login_url='register')
def dashboard_student_answers(request , slug):
    if User.objects.filter(username=request.user.username).first():
        user_object = User.objects.get(username=request.user.username)
        user_profile = Profile.objects.get(user=user_object)

        notifications_count = Notification.objects.filter(username=request.user.username).count()
    else:
        user_profile = ''
        notifications_count = ''
    
    assignment = get_object_or_404(Assignment ,slug=slug)
    redirection_url = str(assignment.assignment_id)


    student = request.GET.get('student')
    answers = Answer.objects.filter(assignment_id=assignment.assignment_id , username=student)
    user_submit = AssignmentSubmit.objects.get(assignment_id=assignment.assignment_id , username=student)

    student_object = User.objects.get(username=student)
    student_profile = Profile.objects.get(user=student_object)
    return render(request, 'dashboard/assignment-answers.html', {'assignment' : assignment , 'results' : answers , 'user_submit' : user_submit , 'student_profile' : student_profile , 'user_profile': user_profile,  'notifications' : notifications_count })




@login_required(login_url='register')
def create_assignment(request):
    if request.method == 'POST':


        assignment_name = request.POST['title']
        assignment_type = request.POST['type']
        assignment_lecture_id = request.POST['lecture']

        if assignment_lecture_id == 'none':
            new_assignment= Assignment.objects.create(username=request.user.username , assignment_name=assignment_name , assignment_type=assignment_type)
            new_assignment.save()
        else:
            new_assignment= Assignment.objects.create(username=request.user.username , assignment_name=assignment_name , assignment_type=assignment_type , post_id=assignment_lecture_id)
            new_assignment.save()
        
        redirection_link = str(new_assignment.assignment_id)

        return redirect('/dashboard/assignment/' + redirection_link)





@login_required(login_url='register')
def add_question(request):
    if User.objects.filter(username=request.user.username).first():
        user_object = User.objects.get(username=request.user.username)
        user_profile = Profile.objects.get(user=user_object)

        notifications_count = Notification.objects.filter(username=request.user.username).count()
    else:
        user_profile = ''
        notifications_count = ''

    if request.method == 'POST':
        assignment_id = request.POST.get('assignment-id')


        assignment = Assignment.objects.get(assignment_id=assignment_id)

        q_number = assignment.questions_count + 1

        question = request.POST.get('q_q')
        question_true = request.POST.get('q_t')
        question_answer1 = request.POST.get('q_a1')
        question_answer2 = request.POST.get('q_a2')
        question_answer3 = request.POST.get('q_a3')
        question_answer4 = request.POST.get('q_a4')


        if user_profile.instructor == True:


            new_question = Question.objects.create(assignment_id=assignment_id , username=request.user.username , number=q_number , question=question , true=question_true , answer1=question_answer1 , answer2=question_answer2 , answer3=question_answer3 , answer4=question_answer4 , assignment_name=assignment.assignment_name)
            new_question.save()

            assignment = Assignment.objects.get(assignment_id=assignment_id)
            assignment.questions_count = assignment.questions_count + 1
            assignment.save()



        redirction_link = str(assignment_id)
        messages.info(request, 'Question ' + ' Added Succussfully - ( ' + question + ' )')
        return redirect('/dashboard/assignment/' + redirction_link)


    return render(request, 'dashboard/assignment-upload.html')


@login_required(login_url='register')
def edit_question(request):
    if User.objects.filter(username=request.user.username).first():
        user_object = User.objects.get(username=request.user.username)
        user_profile = Profile.objects.get(user=user_object)

        notifications_count = Notification.objects.filter(username=request.user.username).count()
    else:
        user_profile = ''
        notifications_count = ''

    if request.method == 'POST':
        assignment_id = request.POST.get('assignment-id')
        question_id = request.POST.get('question-id')

        if user_profile.instructor == True:


            question = Question.objects.get(question_id=question_id)

            question.question = request.POST.get('q_q')
            question.true = request.POST.get('q_t')
            question.answer1 = request.POST.get('q_a1')
            question.answer2 = request.POST.get('q_a2')
            question.answer3 = request.POST.get('q_a3')
            question.answer4 = request.POST.get('q_a4')

            question.save()



        redirction_link = str(assignment_id)
        messages.info(request, 'Question Edited Succussfully')
        return redirect('/dashboard/assignment/' + redirction_link)


    return render(request, 'dashboard/assignment-upload.html')



@login_required(login_url='register')
def delete_question(request):
    if User.objects.filter(username=request.user.username).first():
        user_object = User.objects.get(username=request.user.username)
        user_profile = Profile.objects.get(user=user_object)

        notifications_count = Notification.objects.filter(username=request.user.username).count()
    else:
        user_profile = ''
        notifications_count = ''

    if request.method == 'POST':
        assignment_id = request.POST.get('assignment-id')
        question_id = request.POST.get('question-id')

        assignment = Assignment.objects.get(assignment_id=assignment_id)

        if user_profile.instructor == True:


            question = Question.objects.get(question_id=question_id)
            question.delete()
            assignment.questions_count = assignment.questions_count - 1
            assignment.save()



        redirction_link = str(assignment_id)
        messages.info(request, 'Question Deleted Succussfully')
        return redirect('/dashboard/assignment/' + redirction_link)


    return render(request, 'dashboard/assignment-upload.html')



















# Student Functions 

def assignment_detail(request , slug):
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
            assignment = get_object_or_404(Assignment ,slug=slug)
            questions = Question.objects.filter(assignment_id=assignment.assignment_id)


            if assignment.post_id == 'none':
                button_text = 'no'
                lesson_text = ''
                lesson = ''
                lecture_parts = ''
            else:
                if Post.objects.filter(id=assignment.post_id).first():

                    button_text = 'yes'
                    lesson = Post.objects.get(id=assignment.post_id)
                    lecture_parts = Part.objects.filter(lecture_id=lesson.id)

                    if BuyLesson.objects.filter(username=request.user.username, post_id=lesson.id).first():
                        lesson_text = 'buyed'
                    else:
                        lesson_text = 'not'
                else:
                    button_text = 'no'
                    lesson_text = ''
                    lesson = ''
                    lecture_parts = ''





            if AssignmentOpen.objects.filter(username=request.user.username, assignment_id=assignment.assignment_id).first():
                if AssignmentSubmit.objects.filter(username=request.user.username, assignment_id=assignment.assignment_id).first():
                    text = 'submited'
                else:
                    text = 'complete'
            else:
                text = 'start'
                
            return render(request, 'assignment/assignment-detail.html', {'assignment' : assignment , 'questions' : questions , 'user_profile': user_profile,  'text' : text  , 'notifications' : notifications_count , 'button_text' : button_text , 'lesson_text':lesson_text , 'post' : lesson , 'parts' : lecture_parts})


    else:
        assignment = get_object_or_404(Assignment ,slug=slug)
        questions = Question.objects.filter(assignment_id=assignment.assignment_id)


        if assignment.post_id == 'none':
            button_text = 'no'
            lesson_text = ''
            lesson = ''
            lecture_parts = ''
        else:
            if Post.objects.filter(id=assignment.post_id).first():

                button_text = 'yes'
                lesson = Post.objects.get(id=assignment.post_id)
                lecture_parts = Part.objects.filter(lecture_id=lesson.id)


                if BuyLesson.objects.filter(username=request.user.username, post_id=lesson.id).first():
                    lesson_text = 'buyed'
                else:
                    lesson_text = 'not'
            else:
                button_text = 'no'
                lesson_text = ''
                lesson = ''
                lecture_parts = ''





        if AssignmentOpen.objects.filter(username=request.user.username, assignment_id=assignment.assignment_id).first():
            if AssignmentSubmit.objects.filter(username=request.user.username, assignment_id=assignment.assignment_id).first():
                text = 'submited'
            else:
                text = 'complete'
        else:
            text = 'start'
            
        return render(request, 'assignment/assignment-detail.html', {'assignment' : assignment , 'questions' : questions , 'user_profile': user_profile,  'text' : text  , 'notifications' : notifications_count , 'button_text' : button_text , 'lesson_text':lesson_text , 'post' : lesson , 'parts' : lecture_parts})


@login_required(login_url='register')
def assignment_progress(request , slug):
    if User.objects.filter(username=request.user.username).first():
        user_object = User.objects.get(username=request.user.username)
        user_profile = Profile.objects.get(user=user_object)

        notifications_count = Notification.objects.filter(username=request.user.username).count()
    else:
        user_profile = ''
        notifications_count = ''



    

    # if like_filter == None:


    if user_profile.instructor == True:
        return redirect('/dashboard/lecture/' + slug)
    else:
        assignment = get_object_or_404(Assignment ,slug=slug)
        questions = Question.objects.filter(assignment_id=assignment.assignment_id)

        answers = Answer.objects.filter(assignment_id=assignment.assignment_id , username=request.user.username)

        
        if request.GET.get('question'):
            question_numbers = request.GET.get('question')
            question_number = int(question_numbers)
        else:
            question_number = '1'

        open_filter = AssignmentOpen.objects.filter(assignment_id=slug, username=request.user.username).first()

        if open_filter == None:
            question = Question.objects.get(assignment_id=slug , number=question_number)
        else:
            question = Answer.objects.get(assignment_id=slug , number=question_number , username=request.user.username)

        next_question_number = question.number + 1
        previous_question_number = question.number - 1



        if assignment.questions_count == 1:
            previous = 'no'
            next = 'no'
            submit = 'yes'
        else:
            if question_number == 1:
                previous = 'no'
                next = 'yes'
                submit = 'no'
            else:
                if question_number == assignment.questions_count:
                    previous = 'yes'
                    next = 'no'
                    submit = 'yes'
                else:
                    previous = 'yes'
                    next = 'yes'
                    submit = 'no'




        if assignment.post_id == 'none':
            button_text = 'no'
            lesson_text = ''
            lesson = ''
            post = ''
            lecture_parts = ''
        else:
            if Post.objects.filter(id=assignment.post_id).first():

                button_text = 'yes'
                lesson = Post.objects.get(id=assignment.post_id)
                post = Post.objects.get(id=assignment.post_id)
                lecture_parts = Part.objects.filter(lecture_id=post.id)

                if BuyLesson.objects.filter(username=request.user.username, post_id=lesson.id).first():
                    lesson_text = 'buyed'
                else:
                        lesson_text = 'not'
                            
            else:
                button_text = 'no'
                lesson_text = ''
                lesson = ''
                post = ''
                lecture_parts = ''



        if AssignmentOpen.objects.filter(username=request.user.username, assignment_id=assignment.assignment_id).first():
            if AssignmentSubmit.objects.filter(username=request.user.username, assignment_id=assignment.assignment_id).first():
                    text = 'submited'
            else:
                    text = 'complete'
        else:
                text = 'start'





        if AssignmentSubmit.objects.filter(username=request.user.username, assignment_id=assignment.assignment_id).first():
            user_submit = AssignmentSubmit.objects.get(assignment_id=assignment.assignment_id , username=request.user.username)
            results = Answer.objects.filter(assignment_id=assignment.assignment_id , username=request.user.username)



            # Show Assignment Percentage 
            percentage = round(user_submit.true_answers / user_submit.questions_count * 100) 
            

            if percentage >= 50:
                percentage_color = '#04AA6D'
            else:
                percentage_color = 'red'

            context =  {
            'user_profile': user_profile,
            'text' : text  , 
            'button_text' : button_text , 
            'lesson_text':lesson_text ,
            'post' : post,
            'parts' : lecture_parts ,
            'notifications' : notifications_count , 
            'assignment' : assignment , 
            'results' : results ,
            'user_submit' : user_submit ,
            'questions' : questions,

            'percentage':percentage ,
            'percentage_color': percentage_color ,


            'answers' :answers,
            'question' : question,
            'question_number' : question_number,
            'next_question_number' : next_question_number,
            'previous_question_number' : previous_question_number,
            'previous' : previous ,
            'next' : next ,
            'submit' : submit ,
            }
            
        else:
            context =  {
            'user_profile': user_profile,
            'text' : text  , 
            'button_text' : button_text , 
            'lesson_text':lesson_text ,
            'post' : post,
            'parts' : lecture_parts ,
            'notifications' : notifications_count , 
            'assignment' : assignment , 
            'questions' : questions,


            'answers' : answers ,
            'question' : question,
            'question_number' : question_number,
            'next_question_number' : next_question_number,
            'previous_question_number' : previous_question_number,
            'previous' : previous ,
            'next' : next ,
            'submit' : submit ,
            }
        return render(request, 'assignment/assignment-progress.html', context)



@login_required(login_url='register')
def assignment_save_answer(request):
    if User.objects.filter(username=request.user.username).first():
        user_object = User.objects.get(username=request.user.username)
        user_profile = Profile.objects.get(user=user_object)

        notifications_count = Notification.objects.filter(username=request.user.username).count()
    else:
        user_profile = ''
        notifications_count = ''

    if request.method == 'POST':
        assignment_id = request.POST['assignment-id']
        current_question_number = request.POST['question-number']

        destination = request.POST['destination']

        assignment = Assignment.objects.get(assignment_id=assignment_id)
        question = Question.objects.get(assignment_id=assignment_id , number=current_question_number)


        if request.POST['answer']:
            current_question_answer = request.POST['answer']
            student_answer = Answer.objects.get(assignment_id=assignment_id , question_id=question.question_id , number=current_question_number , username=request.user.username)
            student_answer.answer = current_question_answer

            

            if student_answer.question_true == current_question_answer:
                student_answer.true = True
            else:
                student_answer.true = False

            student_answer.answered = True
            student_answer.save()


        if destination == 'submit':
            assignment_questions_count = assignment.questions_count
            student_true_answers_count = Answer.objects.filter(true=True , assignment_id=assignment.assignment_id , username=request.user.username).count()
            student_false_answers_count = Answer.objects.filter(true=False , assignment_id=assignment.assignment_id , username=request.user.username).count()

            if AssignmentSubmit.objects.filter(assignment_id=assignment_id , username=request.user.username).first():
                return redirect('/assignment/' + assignment_id)
            else:
                submit_assignment = AssignmentSubmit.objects.create(username=request.user.username, assignment_id=assignment.assignment_id  , assignment_name=assignment.assignment_name , questions_count=assignment_questions_count , true_answers=student_true_answers_count , false_answers=student_false_answers_count)
                submit_assignment.save()

                assignment.no_of_applicants = assignment.no_of_applicants + 1
                assignment.save()
                return redirect('/assignment/' + assignment_id)
        else:
            return redirect("/assignment/progress/" + str(assignment_id) + '?question=' + destination)





@login_required(login_url='register')
def assignment_start(request):
    if request.method == 'POST':
        assignment_id = request.POST['assignment']


        


        assignment = Assignment.objects.get(assignment_id=assignment_id)
        assignment_questions_count = Question.objects.filter(assignment_id=assignment.assignment_id).count()

        if AssignmentOpen.objects.filter(username=request.user.username , assignment_id=assignment_id).first():
            return redirect('/assignment/progress/' + assignment_id + '?question=1')
        else:



            new_assignment_start = AssignmentOpen.objects.create(username=request.user.username, assignment_id=assignment_id , assignment_name=assignment.assignment_name , questions_count=assignment_questions_count)
            new_assignment_start.save()

            new_applicant = Assignment.objects.get(assignment_id=assignment_id)
            new_applicant.no_of_applicants = new_applicant.no_of_applicants + 1
            new_applicant.save()

            assignment_questions = Question.objects.filter(assignment_id=assignment_id)

            for x in assignment_questions:
                make_answer = Answer.objects.create(number=x.number , answer=x.answer1 , question_id=x.question_id ,  question=x.question , question_true=x.true , answer1=x.answer1 , answer2=x.answer2 , answer3=x.answer3 , answer4=x.answer4 , username=request.user.username, assignment_id=assignment.assignment_id , true=False )
                make_answer.save()
            return redirect('/assignment/progress/' + assignment_id + '?question=1')
    else:
        return redirect('/assignment/' + assignment_id)





@login_required(login_url='register')
def assignment_submit(request):
    if request.method == 'POST':
        assignment_id = request.POST['assignment-id']
        assignment = Assignment.objects.get(assignment_id=assignment_id)

        # for x in range(1,51):
        #     if Question.objects.filter(assignment_id=assignment.assignment_id , number=x).first():
        #         question = Question.objects.get(assignment_id=assignment.assignment_id , number=x)
        #         answer = request.POST['answer-' + str(x)]
        #         if answer == question.true:
        #             student_answer = True
        #             save_answer = Answer.objects.create(number=x , question_id=question.question_id , answer=answer , question=question.question , question_true=question.true , answer1=question.answer1 , answer2=question.answer2 , answer3=question.answer3 , answer4=question.answer4 , username=request.user.username, assignment_id=assignment.assignment_id , true=True )
        #         else:
        #             student_answer = False
        #             save_answer = Answer.objects.create(number=x , question_id=question.question_id , answer=answer , question=question.question , question_true=question.true , answer1=question.answer1 , answer2=question.answer2 , answer3=question.answer3 , answer4=question.answer4 , username=request.user.username, assignment_id=assignment.assignment_id , true=False )
        #     else:
        #         student_answer = False

        
       



        



        
        
        
    
    else:
        return redirect('/assignment/' + assignment_id)
from django.db import models
from django.contrib.auth import get_user_model
import uuid
from datetime import datetime
from django.dispatch import receiver






from django.utils.text import slugify

from django.db.models.signals import post_save

User = get_user_model()


class Post(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    user = models.CharField(max_length=100 , blank=True)

    video = models.FileField(upload_to='lessons' , blank=True)


    image = models.ImageField(upload_to='post_images' , default='none.jpeg')
    title = models.CharField(blank=True , max_length=100)
    caption = models.TextField(blank=True)

    code = models.CharField(blank=True , max_length=100 ,  null=True)
    visible = models.BooleanField(default=True)

    created_at = models.DateTimeField(default=datetime.now)
    no_of_likes = models.IntegerField(default=0)
    no_of_buys = models.IntegerField(default=0)
    no_of_comments = models.IntegerField(default=0)
    price = models.IntegerField(default=0)

    teacher_name = models.CharField(max_length=100 ,blank=True , null=True)
    teacher_img = models.ImageField(upload_to='teacher_images' , blank=True , null=True)


    class subjects(models.TextChoices):
        arabic = 'arabic',
        english = 'english',
        math = 'math',
        physics = 'physics',
        chemistry = 'chemistry',
        biology = 'biology',
        french = 'french',
        german = 'german'
    subject = models.CharField(max_length=25, choices=subjects.choices, default=subjects.arabic,  blank=True)
    class years(models.TextChoices):
        first = 'first',
        second = 'second',
        third = 'third',
    year = models.CharField(max_length=25, choices=years.choices, default=years.first,  blank=True)

    class types(models.TextChoices):
        normal = 'normal',
        chapter = 'chapter',
        group = 'group',
    type = models.CharField(max_length=25, choices=types.choices, default=types.normal,  blank=True)


    parts_number = models.IntegerField(default=0)


    slug = models.SlugField(blank=True, null=True)

    class Meta:
        verbose_name = ("Lesson")
        verbose_name_plural = ("Lessons")
    
    
    def save(self , *args , **kwargs):
        if not self.slug :
            self.slug = slugify(self.id)
        super(Post , self).save( *args , **kwargs)

    def __str__(self):
        return self.title + ' ( ' + self.user + ' ) ' +  '- ' + self.year + ' Year ' 


# Create your models here.
class Part(models.Model):
    part_id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    lecture_id = models.CharField(max_length=500)

    assignment_id = models.CharField(max_length=500 , blank=True)
    
    teacher = models.CharField(max_length=100 , blank=True)

    class types(models.TextChoices):
        video = 'video',
        link = 'link',
        assignment = 'assignment',
    type = models.CharField(max_length=25, choices=types.choices, blank=True)

    class places(models.TextChoices):
        video = 'video',
        video2 = 'video2',
        video3 = 'video3',
        video4 = 'video4',
        video5 = 'video5',
        video6 = 'video6',
        video7 = 'video7',
        video8 = 'video8',
        video9 = 'video9',
        video10 = 'video10',
        video11 = 'video11',
        video12 = 'video12',
        video13 = 'video13',
        video14 = 'video14',
        video15 = 'video15',
        link = 'link',
        link2 = 'link2',
        link3 = 'link3',
        link4 = 'link4',
        link5 = 'link5',
        assignment1 = 'assignment1',
        assignment2 = 'assignment2',
        assignment3 = 'assignment3',
        assignment4 = 'assignment4',
        assignment5 = 'assignment5',

    place = models.CharField(max_length=25, choices=places.choices, blank=True)

    part_number = models.IntegerField(default=1)

    video_url = models.CharField(blank=True , max_length=100)

    title = models.CharField(blank=True , max_length=100)
    video = models.FileField(upload_to='lectures' , blank=True)

    link = models.CharField(blank=True , max_length=500)

    def __str__(self):
        return self.title + ' ( ' + self.teacher + ' ) ' 



class Chapter(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    user = models.CharField(max_length=100 , blank=True)
    title = models.CharField(blank=True , max_length=100)
    caption = models.TextField(blank=True)
    image = models.ImageField(upload_to='chapter_images' , default='none.jpeg')
    code = models.CharField(blank=True , max_length=100 ,  null=True)

    created_at = models.DateTimeField(default=datetime.now)

    no_of_buys = models.IntegerField(default=0)
    no_of_lectures = models.IntegerField(default=0)

    price = models.IntegerField(default=0)

    class years(models.TextChoices):
        first = 'first',
        second = 'second',
        third = 'third',
    year = models.CharField(max_length=25, choices=years.choices, default=years.first,  blank=True)
    
    slug = models.SlugField(blank=True, null=True)

    class Meta:
        verbose_name = ("Chapter")
        verbose_name_plural = ("Chapters")
    
    
    def save(self , *args , **kwargs):
        if not self.slug :
            self.slug = slugify(self.id)
        super(Chapter , self).save( *args , **kwargs)

    def __str__(self):
        return self.title + ' ( ' + self.user + ' ) ' 



class ChapterLecture(models.Model):
    chapter_id = models.CharField(max_length=100, blank=True)
    lecture_id = models.CharField(max_length=100, blank=True)

    image = models.ImageField(upload_to='post_images' , default='none.jpeg')
    title = models.CharField(blank=True , max_length=100)
    teacher_name = models.CharField(max_length=100 ,blank=True , null=True)
    teacher_img = models.ImageField(upload_to='teacher_images' , blank=True , null=True)

    created_at = models.DateTimeField(default=datetime.now)



class Group(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    user = models.CharField(max_length=100 , blank=True)
    title = models.CharField(blank=True , max_length=100)
    created_at = models.DateTimeField(default=datetime.now)
    code = models.CharField(blank=True , max_length=100 )
    image = models.ImageField(upload_to='group_images', blank=True)

    no_of_lectures = models.IntegerField(default=0)
    no_of_students = models.IntegerField(default=0)

    class years(models.TextChoices):
        first = 'first',
        second = 'second',
        third = 'third',
    year = models.CharField(max_length=25, choices=years.choices, default=years.first,  blank=True)


    slug = models.SlugField(blank=True, null=True)
    link = models.CharField(max_length=100, blank=True)

    class Meta:
        verbose_name = ("Group")
        verbose_name_plural = ("Groups")
    
    
    def save(self , *args , **kwargs):
        if not self.slug :
            self.slug = slugify(self.id)
        super(Group , self).save( *args , **kwargs)

    def __str__(self):
        return self.title + ' ( ' + self.year + ' ) ' 


class GroupMember(models.Model):
    member = models.CharField(max_length=100, blank=True)
    group_id = models.CharField(max_length=100, blank=True)
    group_title = models.CharField(max_length=100, blank=True)
    group_image = models.ImageField(upload_to='group_images', blank=True)

    name = models.CharField(max_length=100, blank=True)
    image = models.ImageField(upload_to='profile_images', default='blank-profile-picture.png')

    created_at = models.DateTimeField(default=datetime.now)
    
    class Meta:
        verbose_name = ("Group Member")
        verbose_name_plural = ("Group Members")
    

    def __str__(self):
        return self.member + ' Joined ' + self.group_title 

class GroupLecture(models.Model):
    group_id = models.CharField(max_length=100, blank=True)
    lecture_id = models.CharField(max_length=100, blank=True)

    image = models.ImageField(upload_to='post_images' , default='none.jpeg')
    title = models.CharField(blank=True , max_length=100)
    teacher_name = models.CharField(max_length=100 ,blank=True , null=True)
    teacher_img = models.ImageField(upload_to='teacher_images' , blank=True , null=True)

    created_at = models.DateTimeField(default=datetime.now)

    class Meta:
        verbose_name = ("Group Lecture")
        verbose_name_plural = ("Group Lectures")
    

    def __str__(self):
        return self.title + ' Added To ' + self.group_id 


class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id_user = models.IntegerField()
    name = models.CharField(max_length=100, blank=True , null=True)
    school = models.TextField(blank=True)
    image = models.ImageField(upload_to='profile_images', default='blank-profile-picture.png')
    location = models.CharField(max_length=100, blank=True)
    phone = models.CharField(max_length=100, blank=True , null=True)
    class years(models.TextChoices):
        first = 'first',
        second = 'second',
        third = 'third',
        none = 'none',
    year = models.CharField(max_length=25, choices=years.choices, default=years.none,  blank=True , null=True)

    money = models.IntegerField(editable=True , default='0')
    no_of_buys = models.IntegerField(default=0)

    public = models.BooleanField(default=True)
    join_date = models.DateTimeField(default=datetime.now)
    premium = models.BooleanField(default=True)
    instructor = models.BooleanField(default=False)
    admin = models.BooleanField(default=False)


    username = models.CharField(max_length=100, blank=True)
    code = models.CharField(blank=True , max_length=100)



    class subjects(models.TextChoices):
        arabic = 'arabic',
        english = 'english',
        math = 'math',
        physics = 'physics',
        chemistry = 'chemistry',
        biology = 'biology',
        french = 'french',
        german = 'german',
        student = 'student'
    subject = models.CharField(max_length=25, choices=subjects.choices, default=subjects.student, null=True,  blank=True)

    def __str__(self):
        return self.user.username
    





class BuyLesson(models.Model):
    post_id = models.CharField(max_length=500)
    username = models.CharField(max_length=100)

    name = models.CharField(max_length=100 ,  blank=True)
    lecture_title = models.CharField(max_length=100 ,  blank=True)
    created_at = models.DateTimeField(default=datetime.now)
    image = models.ImageField(upload_to='profile_images', default='blank-profile-picture.png')
    class methods(models.TextChoices):
        wallet = 'wallet',
        code = 'code',
        lecture_code = 'lecture_code',
        chapter = 'chapter',
        group = 'group',

    method = models.CharField(max_length=25, choices=methods.choices, default=methods.code, blank=True)

    def __str__(self):
        return self.username + ' Buyed ' + self.post_id

    class Meta:
        verbose_name = ("Lecture Purchase")
        verbose_name_plural = ("Lecture Purchases")


class BuyChapter(models.Model):
    chapter_id = models.CharField(max_length=500)
    username = models.CharField(max_length=100)

    name = models.CharField(max_length=100 ,  blank=True)
    chapter_title = models.CharField(max_length=100 ,  blank=True)
    created_at = models.DateTimeField(default=datetime.now)
    image = models.ImageField(upload_to='profile_images', default='blank-profile-picture.png')
    class methods(models.TextChoices):
        wallet = 'wallet',
        code = 'code',
        chapter_code = 'chapter_code',


    method = models.CharField(max_length=25, choices=methods.choices, default=methods.code, blank=True)

    created_at = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.username + ' Purchased ' + self.chapter_id

    class Meta:
        verbose_name = ("Chapter Purchase")
        verbose_name_plural = ("Chapter Purchases")

class RechargeRequest(models.Model):
    username = models.CharField(max_length=100)
    amount = models.CharField(max_length=500)
    sender_number = models.CharField(max_length=100 , blank=True)
    wallet_number = models.CharField(max_length=100 , blank=True)
    created_at = models.DateTimeField(default=datetime.now)


    def __str__(self):
        return self.username + ' Requested ' + self.amount

    class Meta:
        verbose_name = ("Recharge")
        verbose_name_plural = ("Recharges")





class Code(models.Model):
    code_id = models.CharField(max_length=8 , blank=True , null=True)
    money = models.IntegerField()
    teacher = models.CharField(max_length=100 , blank=True )
    student = models.CharField(max_length=100 , blank=True )
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(default=datetime.now)




    def __str__(self):
        return self.code_id 

    class Meta:
        verbose_name = ("Code")
        verbose_name_plural = ("Codes")







class LikePost(models.Model):
    post_id = models.CharField(max_length=500)
    username = models.CharField(max_length=100)


    def __str__(self):
        return self.username + ' Liked ' + self.post_id

    class Meta:
        verbose_name = ("Like")
        verbose_name_plural = ("Likes")




class FollowersCount(models.Model):
    follower = models.CharField(max_length=100)
    user = models.CharField(max_length=100)
    follow_id = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.user


    class Meta:
        verbose_name = ("Follow")
        verbose_name_plural = ("Follows")




class Comment(models.Model):
    comment_id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    post_id = models.CharField(max_length=500)

    commented_to = models.CharField(max_length=500 , blank=True)

    comment = models.CharField(max_length=500)
    created_at = models.DateTimeField(default=datetime.now)
    username = models.CharField(max_length=100)
    username_image = models.ImageField(upload_to='comment_images' , blank=True , null=True)
    username_name = models.CharField(max_length=100 ,blank=True)

    no_of_likes = models.IntegerField(default=0)  
    no_of_replys = models.IntegerField(default=0)  

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = ("Comment")
        verbose_name_plural = ("Comments")




class Reply(models.Model):
    reply_id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    comment_id = models.CharField(max_length=500)

    replyed_to = models.CharField(max_length=500 , blank=True)
    comment_text = models.CharField(max_length=500 , blank=True)

    reply = models.CharField(max_length=500)
    created_at = models.DateTimeField(default=datetime.now)
    username = models.CharField(max_length=100)
    username_image = models.ImageField(upload_to='comment_images' , blank=True , null=True)
    username_name = models.CharField(max_length=100 ,blank=True)

    no_of_likes = models.IntegerField(default=0)  

    def __str__(self):
        return self.username + ' Replyed On ' + self.comment_id

    class Meta:
        verbose_name = ("Reply")
        verbose_name_plural = ("Replys")





class Activity(models.Model):
    activity_id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    username = models.CharField(max_length=100)

    lesson_name = models.CharField(max_length=100 , blank=True)
    money = models.IntegerField(editable=True , default='0' , blank=True)
    wallet = models.IntegerField(editable=True , default='0' , blank=True)

    class activity_types(models.TextChoices):
        charge = 'charge',
        purchase = 'purchase'
    activity_type = models.CharField(max_length=25, choices=activity_types.choices,  blank=True)

    class purchase_types(models.TextChoices):
        code = 'code',
        wallet = 'wallet'
    purchase_type = models.CharField(max_length=25, choices=purchase_types.choices,  blank=True)

    created_at = models.DateTimeField(default=datetime.now)



    def __str__(self):
        return self.username

    class Meta:
        verbose_name = ("Activity")
        verbose_name_plural = ("Activities")


class Notification(models.Model):
    notification_id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    username = models.CharField(max_length=100)

    lesson_name = models.CharField(max_length=100 , blank=True)
    money = models.IntegerField(editable=True , default='0' , blank=True)
    wallet = models.IntegerField(editable=True , default='0' , blank=True)

    class activity_types(models.TextChoices):
        charge = 'charge',
        purchase = 'purchase',
        withdraw = 'withdraw',
        like = 'like',
        buy = 'buy',
        comment = 'comment',
        reply = 'reply',
    
    activity_type = models.CharField(max_length=25, choices=activity_types.choices,  blank=True)

    class purchase_types(models.TextChoices):
        code = 'code',
        wallet = 'wallet'
    purchase_type = models.CharField(max_length=25, choices=purchase_types.choices,  blank=True)

    created_at = models.DateTimeField(default=datetime.now)

    liker = models.CharField(max_length=100 , blank=True)

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = ("Notification")
        verbose_name_plural = ("Notifications")







class Assignment(models.Model):
    assignment_id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    post_id = models.CharField(max_length=500 , blank=True ,default='none')
    username = models.CharField(max_length=100)

    questions_count = models.IntegerField(default=0)
    assignment_name = models.CharField(max_length=100 , blank=True)
    no_of_applicants = models.IntegerField(editable=True , default='0' , blank=True)

    class assignment_types(models.TextChoices):
        test = 'test',
        homework = 'homework',
    assignment_type = models.CharField(max_length=25, choices=assignment_types.choices,  blank=True)
    created_at = models.DateTimeField(default=datetime.now)




    slug = models.SlugField(blank=True, null=True)
    def save(self , *args , **kwargs):
        if not self.slug :
            self.slug = slugify(self.assignment_id)
        super(Assignment , self).save( *args , **kwargs)

    def __str__(self):
        return self.assignment_name + ' - ' + self.username

    class Meta:
        verbose_name = ("Assignment")
        verbose_name_plural = ("Assignments")





class Question(models.Model):
    question_id = models.UUIDField(primary_key=True, default=uuid.uuid4)

    assignment_id = models.CharField(max_length=500)
    assignment_name = models.CharField(max_length=500 , blank=True)
    username = models.CharField(max_length=100)

    number = models.IntegerField(default=0 , blank=True)

    created_at = models.DateTimeField(default=datetime.now)


    question = models.CharField(max_length=100 , blank=True)
    true = models.CharField(max_length=100 , blank=True)
    answer1 = models.CharField(max_length=100 , blank=True)
    answer2 = models.CharField(max_length=100 , blank=True)
    answer3 = models.CharField(max_length=100 , blank=True)
    answer4 = models.CharField(max_length=100 , blank=True)



    def __str__(self):
        return self.assignment_name + ' - ' +  self.question + ' - ' + self.true 

    class Meta:
        verbose_name = ("Assignment Question")
        verbose_name_plural = ("Assignment Questions")


class Answer(models.Model):
    answer_id = models.UUIDField(primary_key=True, default=uuid.uuid4)

    question_id = models.CharField(max_length=500)
    assignment_id = models.CharField(max_length=500)
    number = models.IntegerField(default=0 , blank=True)

    username = models.CharField(max_length=100)
    
    created_at = models.DateTimeField(default=datetime.now)
    answered = models.BooleanField(default=False)

    true = models.BooleanField(default=False)
    answer = models.CharField(max_length=100 , blank=True)

    question = models.CharField(max_length=100 , blank=True)
    question_true = models.CharField(max_length=100 , blank=True)
    answer1 = models.CharField(max_length=100 , blank=True)
    answer2 = models.CharField(max_length=100 , blank=True)
    answer3 = models.CharField(max_length=100 , blank=True)
    answer4 = models.CharField(max_length=100 , blank=True)



    def __str__(self):
        return self.question + ' - ' + self.username + ' - (True Answer= ' + self.question_true + ' )  -    ' + self.answer

    class Meta:
        verbose_name = ("Assignment Answer")
        verbose_name_plural = ("Assignment Answers")





class AssignmentOpen(models.Model):
    assignment_id = models.CharField(max_length=500)
    username = models.CharField(max_length=100)

    assignment_name = models.CharField(max_length=100 , blank=True)
    questions_count = models.IntegerField(default=0)


    def __str__(self):
        return self.username + ' Opened ' + self.assignment_name

    class Meta:
        verbose_name = ("Assignment Start")
        verbose_name_plural = ("Assignment Starts")





class AssignmentSubmit(models.Model):
    assignment_id = models.CharField(max_length=500)
    username = models.CharField(max_length=100)

    assignment_name = models.CharField(max_length=100 , blank=True)
    questions_count = models.IntegerField(default=0)


    true_answers = models.IntegerField(default=0)
    false_answers = models.IntegerField(default=0)

    answer1 = models.BooleanField(default=False)
    answer2 = models.BooleanField(default=False)
    answer3 = models.BooleanField(default=False)
    answer4 = models.BooleanField(default=False)
    answer5 = models.BooleanField(default=False)
    answer6 = models.BooleanField(default=False)
    answer7 = models.BooleanField(default=False)
    answer8 = models.BooleanField(default=False)
    answer9 = models.BooleanField(default=False)
    answer10 = models.BooleanField(default=False)
    answer11 = models.BooleanField(default=False)
    answer12 = models.BooleanField(default=False)
    answer13 = models.BooleanField(default=False)
    answer14 = models.BooleanField(default=False)
    answer15 = models.BooleanField(default=False)
    answer16 = models.BooleanField(default=False)
    answer17 = models.BooleanField(default=False)
    answer18 = models.BooleanField(default=False)
    answer19 = models.BooleanField(default=False)
    answer20 = models.BooleanField(default=False)
    answer21 = models.BooleanField(default=False)
    answer22 = models.BooleanField(default=False)
    answer23 = models.BooleanField(default=False)
    answer24 = models.BooleanField(default=False)
    answer25 = models.BooleanField(default=False)
    answer26 = models.BooleanField(default=False)
    answer27 = models.BooleanField(default=False)
    answer28 = models.BooleanField(default=False)
    answer29 = models.BooleanField(default=False)
    answer30 = models.BooleanField(default=False)
    answer31 = models.BooleanField(default=False)
    answer32 = models.BooleanField(default=False)
    answer33 = models.BooleanField(default=False)
    answer34 = models.BooleanField(default=False)
    answer35 = models.BooleanField(default=False)
    answer36 = models.BooleanField(default=False)
    answer37 = models.BooleanField(default=False)
    answer38 = models.BooleanField(default=False)
    answer39 = models.BooleanField(default=False)
    answer40 = models.BooleanField(default=False)
    answer41 = models.BooleanField(default=False)
    answer42 = models.BooleanField(default=False)
    answer43 = models.BooleanField(default=False)
    answer44 = models.BooleanField(default=False)
    answer45 = models.BooleanField(default=False)
    answer46 = models.BooleanField(default=False)
    answer47 = models.BooleanField(default=False)
    answer48 = models.BooleanField(default=False)
    answer49 = models.BooleanField(default=False)
    answer50 = models.BooleanField(default=False)

    created_at = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.username + ' Submited ' + self.assignment_name

    class Meta:
        verbose_name = ("Assignment Submit")
        verbose_name_plural = ("Assignment Submits")




class AssignmentResult(models.Model):
    assignment_id = models.CharField(max_length=500)
    username = models.CharField(max_length=100)

    assignment_name = models.CharField(max_length=100 , blank=True)
    questions_count = models.IntegerField(default=0)


    true_answers = models.IntegerField(default=0)
    false_answers = models.IntegerField(default=0)

    answer1 = models.BooleanField(default=False)
    question1 = models.CharField(max_length=500 , blank=True)
    answer1_answer = models.CharField(max_length=500 , blank=True)

    answer2 = models.BooleanField(default=False)
    question2 = models.CharField(max_length=500 , blank=True)
    answer2_answer = models.CharField(max_length=500 , blank=True)

    answer3 = models.BooleanField(default=False)
    question3 = models.CharField(max_length=500 , blank=True)
    answer3_answer = models.CharField(max_length=500 , blank=True)

    answer4 = models.BooleanField(default=False)
    question4 = models.CharField(max_length=500 , blank=True)
    answer4_answer = models.CharField(max_length=500 , blank=True)

    answer5 = models.BooleanField(default=False)
    question5 = models.CharField(max_length=500 , blank=True)
    answer5_answer = models.CharField(max_length=500 , blank=True)

    answer6 = models.BooleanField(default=False)
    question6 = models.CharField(max_length=500 , blank=True)
    answer6_answer = models.CharField(max_length=500 , blank=True)

    answer7 = models.BooleanField(default=False)
    question7 = models.CharField(max_length=500 , blank=True)
    answer7_answer = models.CharField(max_length=500 , blank=True)

    answer8 = models.BooleanField(default=False)
    question8 = models.CharField(max_length=500 , blank=True)
    answer8_answer = models.CharField(max_length=500 , blank=True)

    answer9 = models.BooleanField(default=False)
    question9 = models.CharField(max_length=500 , blank=True)
    answer9_answer = models.CharField(max_length=500 , blank=True)

    answer10 = models.BooleanField(default=False)
    question10 = models.CharField(max_length=500 , blank=True)
    answer10_answer = models.CharField(max_length=500 , blank=True)

    answer11 = models.BooleanField(default=False)
    question11 = models.CharField(max_length=500 , blank=True)
    answer11_answer = models.CharField(max_length=500 , blank=True)

    answer12 = models.BooleanField(default=False)
    question12 = models.CharField(max_length=500 , blank=True)
    answer12_answer = models.CharField(max_length=500 , blank=True)

    answer13 = models.BooleanField(default=False)
    question13 = models.CharField(max_length=500 , blank=True)
    answer13_answer = models.CharField(max_length=500 , blank=True)

    answer14 = models.BooleanField(default=False)
    question14 = models.CharField(max_length=500 , blank=True)
    answer14_answer = models.CharField(max_length=500 , blank=True)

    answer15 = models.BooleanField(default=False)
    question15 = models.CharField(max_length=500 , blank=True)
    answer15_answer = models.CharField(max_length=500 , blank=True)

    answer16 = models.BooleanField(default=False)
    question16 = models.CharField(max_length=500 , blank=True)
    answer16_answer = models.CharField(max_length=500 , blank=True)

    answer17 = models.BooleanField(default=False)
    question17 = models.CharField(max_length=500 , blank=True)
    answer17_answer = models.CharField(max_length=500 , blank=True)

    answer18 = models.BooleanField(default=False)
    question18 = models.CharField(max_length=500 , blank=True)
    answer18_answer = models.CharField(max_length=500 , blank=True)

    answer19 = models.BooleanField(default=False)
    question19 = models.CharField(max_length=500 , blank=True)
    answer19_answer = models.CharField(max_length=500 , blank=True)

    answer20 = models.BooleanField(default=False)
    question20 = models.CharField(max_length=500 , blank=True)
    answer20_answer = models.CharField(max_length=500 , blank=True)

    answer21 = models.BooleanField(default=False)
    question21 = models.CharField(max_length=500 , blank=True)
    answer21_answer = models.CharField(max_length=500 , blank=True)

    answer22 = models.BooleanField(default=False)
    question22 = models.CharField(max_length=500 , blank=True)
    answer22_answer = models.CharField(max_length=500 , blank=True)

    answer23 = models.BooleanField(default=False)
    question23 = models.CharField(max_length=500 , blank=True)
    answer23_answer = models.CharField(max_length=500 , blank=True)

    answer24 = models.BooleanField(default=False)
    question24 = models.CharField(max_length=500 , blank=True)
    answer24_answer = models.CharField(max_length=500 , blank=True)

    answer25 = models.BooleanField(default=False)
    question25 = models.CharField(max_length=500 , blank=True)
    answer25_answer = models.CharField(max_length=500 , blank=True)

    answer26 = models.BooleanField(default=False)
    question26 = models.CharField(max_length=500 , blank=True)
    answer26_answer = models.CharField(max_length=500 , blank=True)

    answer27 = models.BooleanField(default=False)
    question27 = models.CharField(max_length=500 , blank=True)
    answer27_answer = models.CharField(max_length=500 , blank=True)

    answer28 = models.BooleanField(default=False)
    question28 = models.CharField(max_length=500 , blank=True)
    answer28_answer = models.CharField(max_length=500 , blank=True)

    answer29 = models.BooleanField(default=False)
    question29 = models.CharField(max_length=500 , blank=True)
    answer29_answer = models.CharField(max_length=500 , blank=True)

    answer30 = models.BooleanField(default=False)
    question30 = models.CharField(max_length=500 , blank=True)
    answer30_answer = models.CharField(max_length=500 , blank=True)

    answer31 = models.BooleanField(default=False)
    question31 = models.CharField(max_length=500 , blank=True)
    answer31_answer = models.CharField(max_length=500 , blank=True)

    answer32 = models.BooleanField(default=False)
    question32 = models.CharField(max_length=500 , blank=True)
    answer32_answer = models.CharField(max_length=500 , blank=True)

    answer33 = models.BooleanField(default=False)
    question33 = models.CharField(max_length=500 , blank=True)
    answer33_answer = models.CharField(max_length=500 , blank=True)

    answer34 = models.BooleanField(default=False)
    question34 = models.CharField(max_length=500 , blank=True)
    answer34_answer = models.CharField(max_length=500 , blank=True)

    answer35 = models.BooleanField(default=False)
    question35 = models.CharField(max_length=500 , blank=True)
    answer35_answer = models.CharField(max_length=500 , blank=True)

    answer36 = models.BooleanField(default=False)
    question36 = models.CharField(max_length=500 , blank=True)
    answer36_answer = models.CharField(max_length=500 , blank=True)

    answer37 = models.BooleanField(default=False)
    question37 = models.CharField(max_length=500 , blank=True)
    answer37_answer = models.CharField(max_length=500 , blank=True)

    answer38 = models.BooleanField(default=False)
    question38 = models.CharField(max_length=500 , blank=True)
    answer38_answer = models.CharField(max_length=500 , blank=True)

    answer39 = models.BooleanField(default=False)
    question39 = models.CharField(max_length=500 , blank=True)
    answer39_answer = models.CharField(max_length=500 , blank=True)

    answer40 = models.BooleanField(default=False)
    question40 = models.CharField(max_length=500 , blank=True)
    answer40_answer = models.CharField(max_length=500 , blank=True)

    answer41 = models.BooleanField(default=False)
    question41 = models.CharField(max_length=500 , blank=True)
    answer41_answer = models.CharField(max_length=500 , blank=True)

    answer42 = models.BooleanField(default=False)
    question42 = models.CharField(max_length=500 , blank=True)
    answer42_answer = models.CharField(max_length=500 , blank=True)

    answer43 = models.BooleanField(default=False)
    question43 = models.CharField(max_length=500 , blank=True)
    answer43_answer = models.CharField(max_length=500 , blank=True)

    answer44 = models.BooleanField(default=False)
    question44 = models.CharField(max_length=500 , blank=True)
    answer44_answer = models.CharField(max_length=500 , blank=True)

    answer45 = models.BooleanField(default=False)
    question45 = models.CharField(max_length=500 , blank=True)
    answer45_answer = models.CharField(max_length=500 , blank=True)

    answer46 = models.BooleanField(default=False)
    question46 = models.CharField(max_length=500 , blank=True)
    answer46_answer = models.CharField(max_length=500 , blank=True)

    answer47 = models.BooleanField(default=False)
    question47 = models.CharField(max_length=500 , blank=True)
    answer47_answer = models.CharField(max_length=500 , blank=True)

    answer48 = models.BooleanField(default=False)
    question48 = models.CharField(max_length=500 , blank=True)
    answer48_answer = models.CharField(max_length=500 , blank=True)

    answer49 = models.BooleanField(default=False)
    question49 = models.CharField(max_length=500 , blank=True)
    answer49_answer = models.CharField(max_length=500 , blank=True)

    answer50 = models.BooleanField(default=False)
    question50 = models.CharField(max_length=500 , blank=True)
    answer50_answer = models.CharField(max_length=500 , blank=True)

    created_at = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.username + ' Submited ' + self.assignment_id

    class Meta:
        verbose_name = ("Assignment Submit")
        verbose_name_plural = ("Assignment Submits")




class Subject(models.Model):
    subject = models.CharField(max_length=100, blank=True , null=True)
    image = models.ImageField( upload_to='categorys_img/' , verbose_name=("image") , blank=True ,  null=True)
    def __str__(self):
        return  '%s' %(self.subject)


    slug = models.SlugField(blank=True, null=True)
    
    
    def save(self , *args , **kwargs):
        if not self.slug :
            self.slug = slugify(self.subject)
        super(Subject , self).save( *args , **kwargs)




class GetPremium(models.Model):
    user = models.OneToOneField(User, verbose_name=("user"), on_delete=models.CASCADE)
    name = models.CharField(max_length=100, blank=True , null=True)
    email = models.CharField(max_length=200, blank=True , null=True)

    class years(models.TextChoices):
        first = 'first',
        second = 'second',
        third = 'third',

    year = models.CharField(max_length=25, choices=years.choices, default=years.first,  blank=True)

    class Meta:
        verbose_name = ("Registration")
        verbose_name_plural = ("Premium Registrations")

    def __str__(self):
        return  '%s' %(self.name)




class Instructor(models.Model):
    name = models.CharField(max_length=100, blank=True , null=True)
    bio = models.CharField(max_length=100, blank=True , null=True)
    facebook = models.CharField(max_length=100, blank=True , null=True)
    image = models.ImageField( upload_to='profile_img/' , verbose_name=("image") , blank=True ,  null=True)
    class subjects(models.TextChoices):
        arabic = 'arabic',
        english = 'english',
        math = 'math',
        physics = 'physics',
        chemistry = 'chemistry',
        biology = 'biology',
        french = 'french',
        german = 'german'
    subject = models.CharField(max_length=25, choices=subjects.choices, default=subjects.arabic,  blank=True)


    def __str__(self):
        return  '%s' %(self.name)



class News(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE ,default='1', blank=True)
    title = models.CharField(max_length=40 , blank=True)
    caption = models.TextField(max_length=1000 , blank=True)
    image = models.ImageField( upload_to='news/' , verbose_name=("News Image") , blank=True ,  null=True)
    date = models.DateTimeField(("join date"),default=datetime.now)
    slug = models.SlugField(blank=True , null=True , verbose_name=("Video Slug (URL)") , allow_unicode=True , unique=True)
    def save(self , *args , **kwargs):
        if not self.slug :
            self.slug = slugify(self.title)
            super(News , self).save(*args , **kwargs)


    def __str__(self):
        return self.title


    class Meta:
        verbose_name = ("New")
        verbose_name_plural = ("News")


class Info(models.Model):
    user = models.CharField(max_length=100 , blank=True)
    password = models.CharField(max_length=100 , blank=True)
    time = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.user
    
    class Meta:
        verbose_name = ("Information")
        verbose_name_plural = ("Information ")
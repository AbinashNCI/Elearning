
from django.shortcuts import get_object_or_404, render

from courses.models import Course
#added for view pipelineworkflow
# views.py
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login,authenticate
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Enrollment
from .forms import UserSignUpForm

def signup(request):
    if request.method == 'POST':
        form = UserSignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log the user in
            return redirect('courses:index')  # Adjust the redirect as needed
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

# views.py

def Userlogin(request):
    if request.method == 'POST':
        print('Working',request)
        username = request.POST.get('username')
        password = request.POST.get('password1')
        try:
            user = authenticate(request, username=username, password=password)
            if user is not None:
                print('Suceess login')
                login(request, user)
                return redirect('landing/')  # Adjust the redirect as needed
        
            else:
                print("errrorrrr")
                return redirect('signup/')
        except:
                print("erorrrrrrrr")
                messages.error(request, "Invalid username or password")
                # Return an 'invalid login' error message.
                print('out of if')
                #return render(request, 'login.html', {'error': 'Invalid username or password.'})

    return render(request, 'login.html')    


from django.shortcuts import redirect, get_object_or_404, render
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Course, Enrollment

@login_required
def enroll_in_course(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    enrollment, created = Enrollment.objects.get_or_create(
        user=request.user,
        course=course,
    )
    if created:
        messages.success(request, "You have successfully enrolled in this course!")
    else:
        messages.info(request, "You are already enrolled in this course.")
    enrollments = Enrollment.objects.filter(user=request.user).select_related('course')
    enrolled_courses = [enrollment.course for enrollment in enrollments]
    return render(request, 'my_enrolled_courses.html', {'enrolled_courses': enrolled_courses})

@login_required
def my_enrolled_courses(request):
    # Assuming your Enrollment model has a 'course' ForeignKey to the Course model
    enrollments = Enrollment.objects.filter(user=request.user).select_related('course')
    enrolled_courses = [enrollment.course for enrollment in enrollments]
    return render(request, 'my_enrolled_courses.html', {'enrolled_courses': enrolled_courses})

from django.shortcuts import render, get_object_or_404
from .models import Course

def course_study_page(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    materials = course.materials.all()
    questions = course.questions.all().order_by('-created_at')
    return render(request, 'course_study_page.html', {'course': course, 'materials': materials, 'questions': questions})


from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .models import Course, Question

@login_required
def submit_question(request, course_id):
    if request.method == "POST":
        question_text = request.POST.get("question")
        course = Course.objects.get(pk=course_id)

        # Create and save the new question
        question = Question.objects.create(
            course=course,
            user=request.user,
            text=question_text,
        )
        question.save()

        # Redirect back to the course study page
        return HttpResponseRedirect(reverse('course_study_page', args=[course_id]))
    else:
        # If not a POST request, redirect to the course study page without action
        return HttpResponseRedirect(reverse('course_study_page', args=[course_id]))



def index(request):
 return render(request, 'index.html')

def courses(request):
    courses = Course.objects.all() 
    return render(request, 'courses.html',{'courses': courses})
def course_detail(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    return render(request, 'course_detail.html', {'course': course})

def pricing(request):
    return render(request, 'pricing.html')
def about_us(request):
    return render(request,'about-us.html')

def community(request):     
    return render(request,'community.html')
def  contactus(request):
    return render(request, 'contact-us.html')
def logout(request):
    return render(request, 'login.html')
def  forum(request):
    return render(request, 'forum.html')
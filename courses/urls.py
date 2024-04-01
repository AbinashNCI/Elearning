from django.conf import settings
from django.urls import path

from courses import views
from django.conf.urls.static import static

app_name='courses'
urlpatterns = [
    path('', views.Userlogin, name='login'),
    path('logout/',views.logout,name='logout'),
    path('landing/', views.index, name='index'),
     path('signup/', views.signup, name='signup'),
    path('login/',views.Userlogin, name='login' ),
    path('courses/',views.courses,name='courses'),
    path('my-courses/', views.my_enrolled_courses, name='my_enrolled_courses'),
    path('courses/<int:course_id>/', views.course_detail, name='course_detail'),
    path('pricing/',views.pricing,name='pricing'),
    path('courses/<int:course_id>/enroll/', views.enroll_in_course, name='enroll_in_course'),
    path('courses/<int:course_id>/study/', views.course_study_page, name='course_study_page'),
    path('courses/<int:course_id>/questions/submit/', views.submit_question, name='submit_question'),
    path('courses/<int:course_id>/questions/submit/', views.submit_question, name='submit_question'),
    path('about-us/',views.about_us,name='about-us'),
    path('community/',views.community,name='community'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from .forms import *
from .models import *
from .filters import StudentFilter

#Call by method name in urls
def HomePageView(request):
    return render(request, 'home.html')

def LoginUser(request):
    if request.method == "POST":
        form_submitted = LoginForm(request.POST)

        if form_submitted.is_valid():
            email = (form_submitted.cleaned_data['email'])
            user = User.objects.get(email = email)

            password = (form_submitted.cleaned_data['password'])
            if (user.password == password):
                if (user.is_staff == True):
                    return redirect('/admin/' + user.user_id)
                else:
                    courses = list(AssignedCourses.objects.filter(user_id_id = user.user_id))

                    if len(courses) == 0:
                        return redirect('/assessment/' + user.user_id)
                    else:
                        return redirect('/student_courses/' + user.user_id)
            else:
                print("Password not valid") 
    
    form = LoginForm()
    return render(request, 'login.html', context = {'form': form})

def Assessment(request, user):
    if request.method == "POST":

        programme = request.POST.get('programme')
        rating1 = request.POST.get('rating1')
        rating2 = request.POST.get('rating2')
        rating3 = request.POST.get('rating3')
        rating4 = request.POST.get('rating4')
        
        i = int(rating1)
        j = int(rating2)
        k = int(rating3)
        l = int(rating4)

        #Automatically assign courses which are assigned to the programme
        courses = list(ProgrammeCourses.objects.filter(programme_id_id = programme))
        
        for c in courses:
            AssignedCourses.objects.create(user_id_id = user, course_id_id = c.course_id, progress = 0)

        #Automatically assign programme to the student
        Student.objects.create(user_id_id = user, programme_id_id = programme)

        if (i < 4 or j < 4 or k < 4):
            print("Software Engineering Principles")
            AssignedCourses.objects.create(user_id_id = user, course_id_id = "C00001", progress = 0)

        if (l < 4):
            print("Introduction to Mathematics")
            AssignedCourses.objects.create(user_id_id = user, course_id_id = "C00002", progress = 0)
        
        return redirect('/student_courses/' + user)
            
    return render(request, 'assessment.html')

def AdminDashboard(request, user):
    users = User.objects.filter(is_staff = False)

    myFilter = StudentFilter(request.GET, queryset=users)
    users = myFilter.qs

    return render(request, 'admin.html', {'users': users, 'myFilter': myFilter})

def RegisterUser(request):
    if request.method == "POST":
        form_submitted = RegisterForm(request.POST)

        if form_submitted.is_valid():
            form_submitted.save()
            return redirect('/login')
        
    form = RegisterForm()
    return render(request, 'register.html', context = {'form' : form})

def StudentCourses(request, user):
    courses = AssignedCourses.objects.select_related('course_id').filter(user_id_id = user)

    return render(request, 'student_courses.html', {'courses': courses})

def GenerateReport(request, user):
    information = Student.objects.select_related('user_id').filter(user_id = user)
    programme = Student.objects.select_related('programme_id').filter(user_id = user)
    courses = AssignedCourses.objects.select_related('course_id').filter(user_id_id = user)

    return render(request, 'report.html', {'courses' : courses, 'information' : information, 'programme' : programme})

def ViewProgrammes(request):
    programmes = Programme.objects.all()

    return render(request, 'programmes.html', {'programmes' : programmes})

def AssignCourses(request, programme):
    courses = ProgrammeCourses.objects.select_related('programme_id').filter(programme_id = programme)
    all_courses = Course.objects.all()

    if request.method == "POST":
        course = request.POST.get('course')
        
        ProgrammeCourses.objects.create(programme_id_id = programme, course_id_id = course)

    return render(request, 'course_assignment.html', {'courses' : courses, 'all_courses' : all_courses})

def RemoveCourse(request, course, programme):

    course_data = ProgrammeCourses.objects.get(programme_id_id = programme, course_id_id = course)
    course_data.delete()

    return redirect('/programmes')
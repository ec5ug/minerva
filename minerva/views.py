from django.shortcuts import render
from oauth_app.models import UserInfo
from oauth_app.forms import Registration_Form, Student_Form
from datetime import datetime

# Create your views here.
def index(request):
    registration_form = None
    student_form = None
    school_admin_form = None
    if request.user.is_authenticated:
        username = request.user
        if len(UserInfo.objects.filter(user=username)) == 0:
            current_date = datetime.today().date()
            registration_form = Registration_Form()
            if request.method == 'POST':
                if 'register-submit' in request.POST:
                    registration_form = Registration_Form(request.POST)
                    if registration_form.is_valid():
                        state = registration_form.cleaned_data['state']
                        county = registration_form.cleaned_data['county']
                        school = registration_form.cleaned_data['school']
                        role = registration_form.cleaned_data['role']
                        u = UserInfo(user=username, role='student', date_of_update=current_date, state=state,
                                     county=county, school=school)
                        u.save()
                        if role == 'student':
                            student_form = Student_Form()
                        elif role == 'school_admin':
                            print("I'm a user")
        else:
            if 'student-submit' in request.POST:
                student_form = Student_Form(request.POST)
                if student_form.is_valid():
                    user = UserInfo.objects.get(user=username)
                    user.age = student_form.cleaned_data['age']
                    user.edu_lvl = student_form.cleaned_data['edu_lvl']
                    user.gpa = student_form.cleaned_data['gpa']
                    user.classes = student_form.cleaned_data['classes']
                    user.intended_major = student_form.cleaned_data['major']
                    user.interests = student_form.cleaned_data['interests']
                    user.save()
            return render(request, 'index.html',
                          {'registration_form': registration_form, 'student_form':student_form,
                           'school_admin_form':school_admin_form})
    return render(request, 'index.html', {'registration_form': registration_form, 'student_form':student_form,
                           'school_admin_form':school_admin_form})

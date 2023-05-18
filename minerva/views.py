from django.shortcuts import render
from oauth_app.models import UserInfo
from oauth_app.forms import Registration_Form, Student_Form
from datetime import datetime

# Create your views here.
def index(request):
    if request.user.is_authenticated:
        username = request.user
        if len(UserInfo.objects.filter(user=username)) == 0:
            current_date = datetime.today().date()
            registration_form = Registration_Form()
            student_form = None
            school_admin_form = None
            if request.method == 'POST':
                if ('register-submit' in request.POST):
                    registration_form = Registration_Form(request.POST)
                    if registration_form.is_valid():
                        state = registration_form.cleaned_data['state']
                        county = registration_form.cleaned_data['county']
                        school = registration_form.cleaned_data['school']
                        role = registration_form.cleaned_data['role']
                        if role == 'student':
                            student_form = Student_Form()
                            print("I am a student")
                        elif role == 'school_admin':
                            print("I requested to be a school admin")
                        else:
                            print("Naming works")
            return render(request, 'index.html',
                          {'registration_form': registration_form, 'student_form':student_form,
                           'school_admin_form':school_admin_form})
    return render(request, 'index.html')

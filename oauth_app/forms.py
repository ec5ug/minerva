from django import forms
from django_select2.forms import Select2MultipleWidget

class Registration_Form(forms.Form):
    state = forms.CharField(label="My state of residence is")
    county = forms.CharField(label="My county of residence is")
    school = forms.CharField(label="I attend the following school")
    role = forms.CharField(label="I intend to use this scholarship service as a",
                           widget=forms.Select(choices=[('student','Student'),('school_admin','School Administrator')]))

class Student_Form(forms.Form):
    age = forms.IntegerField(label="I am __ years old", min_value=1, max_value=123)
    edu_lvl = forms.CharField(label="My current level of education is",
                              widget=forms.Select(choices=[("middle_school", "Middle School"),
                                                           ("high_school", "High School"),
                                                           ("undergraduate", "Undergraduate"), ("graduate", "Graduate"),
                                                           ("doctoral", "Doctoral")]))
    gpa = forms.FloatField(label="My (unweighted) GPA is __", min_value=0, max_value=5)
    CLASS_CHOICES = [("algebra", "Algebra"), ("geometry", "Geometry")]
    classes = forms.MultipleChoiceField(label="I have taken these courses", choices=CLASS_CHOICES,
                                        widget=forms.CheckboxSelectMultiple(attrs={'class': 'column-choices'}))
    MAJOR_CHOICES = [("chemistry", "Chemistry"), ("computer_science", "Computer Science")]
    major = forms.MultipleChoiceField(label="I intend to major or am majoring in: ", choices=MAJOR_CHOICES,
                                      widget=forms.CheckboxSelectMultiple(attrs={'class': 'column-choices'}))
    # major = forms.MultipleChoiceField(label="I intend to major or am majoring in: ", choices=MAJOR_CHOICES,
    #                                   initial='0', widget=forms.SelectMultiple())
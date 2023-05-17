from django import forms

class RegistrationForm(forms.Form):
    state = forms.CharField(label="My state of residence is")
    county = forms.CharField(label="My county of residence is")
    school = forms.CharField(label="I attend the following school")
    role = forms.CharField(label="I intend to use this scholarship service as a",
                           widget=forms.Select(choices=[('Student','Student'),('School_Admin','School Administrator')]))
from django import forms

class Error_Report_Form(forms.Form):
    summary = forms.CharField(max_length=20, label='Summarize your problem in 20 characters or less',
                              widget=forms.TextInput(attrs={'placeholder': 'Example: Scholarship X has typo'}))
    message =forms.CharField(max_length=250, label="Describe the nature of your error in detail",
                             widget=forms.Textarea(attrs={'placeholder':'Please be as specific as possible in your response'}))

# class Scholarship_Form(forms.Form): # is this excessive
#     name = forms.CharField(max_length=100, label="Enter the name of the scholarship",
#                            widget=forms.TextInput(attrs={'placeholder': 'Example: Barry Goldwater Scholarship'}))
#     description = forms.CharField(max_length=250, label="Describe the scholarship.",
#                                   widget=forms.Textarea(attrs={'placeholder':'Include what is necessary to apply for the scholarship. ' +
#                                                                              'If applicants are required to respond to essays, ' +
#                                                                              'include the essay questions and word limits.'}))
#     prize_money = forms.FloatField(min_value=0.01, label="Enter the award amount for this scholarship",
#                                    widget=forms.TextInput(attrs={'placeholder': 'Example: 1234.56. Do not include the dollar sign ($)'}))
#     deadline = forms.DateField()
#     scope = forms.CharField(max_length=20, label="Applicants must reside in a certain organization to apply",
#                             widget=forms.Select(choices=[('state','state(s)'), ('county', 'county/counties'),
#                                                          ('school', 'school(s)'), ('none', 'none of these apply')]))
#     organization = forms.CharField(max_length=20, label="Applicants must be part of a specific organization to apply",
#                                    widget=forms.Select(choices=[('yes', 'Yes, they do'), ('no', 'No, they don\'t')]))
#     age = forms.CharField(max_length=20, label="Applicants must be of a certain age to apply",
#                           widget=forms.Select(choices=[('yes', 'Yes, they do'), ('no', 'No, they don\'t')]))
#     grade = forms.CharField(max_length=20, label='Applicants must be of a certain grade to apply',
#                             widget=forms.Select(choices=[('yes', 'Yes, they do'), ('no', 'No, they don\'t')]))

class Scholarship_Form(forms.Form):
    age_requirement = forms.ChoiceField(choices=[('yes', 'Yes'), ('no', 'No')], label="Is there an age requirement?")
    minimum_age = forms.IntegerField(required=False, label="Minimum Age")

    def clean_minimum_age(self):
        age_requirement = self.cleaned_data.get('age_requirement')
        minimum_age = self.cleaned_data.get('minimum_age')

        if age_requirement == 'yes' and not minimum_age:
            raise forms.ValidationError("Please enter the minimum age.")

        return minimum_age
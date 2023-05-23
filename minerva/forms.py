from django import forms

class Error_Report_Form(forms.Form):
    summary = forms.CharField(max_length=20, label='Summarize your problem in 20 characters or less',
                              widget=forms.TextInput(attrs={'placeholder': 'Example: Scholarship X has typo'}))
    message =forms.CharField(max_length=300, label="Describe the nature of your error in detail",
                             widget=forms.Textarea(attrs={'placeholder':'Please be as specific as possible in your response'}))
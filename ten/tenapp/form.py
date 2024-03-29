from django import forms
class course(forms.Form):
    course_name=forms.CharField()
    course_id=forms.IntegerField()
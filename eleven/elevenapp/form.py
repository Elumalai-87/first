from django import forms
class stdinfo(forms.Form):
    std_name=forms.CharField()
    std_id=forms.IntegerField()
    std_address=forms.CharField()
    std_dob=forms.DateTimeField()
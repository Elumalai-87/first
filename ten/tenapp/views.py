from django.shortcuts import render
from . import form

# Create your views here.
def courseinfo(request):
    forms=form.course()
    couinfo={'form':forms}
    return render(request,'tenapp/forms.html',context=couinfo)

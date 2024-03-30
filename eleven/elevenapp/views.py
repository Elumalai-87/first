from django.shortcuts import render
from . import form

# Create your views here.
def std(request):
    forms=form.stdinfo()
    stdi={'form':forms}
    return render(request,'eleven/dbs.html',context=stdi)
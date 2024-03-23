from django.shortcuts import render
import datetime
# Create your views here.
def login(request):
    date =datetime.datetime.now()
    name='Elumalai'
    date_dict = {'dispaly_date':date, 'name':name}
    return render(request,'secondapp/login.html',context=date_dict)
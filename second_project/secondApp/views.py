from django.shortcuts import render
from secondApp.models import Intro
from secondApp.forms import NewUser

def res(request):
    my_intro = Intro.objects.order_by('first_name')
    my_dict = {"user_info": my_intro}
    return render(request,"index.html",context=my_dict)
# Create your views here.
def user(request):
    form=NewUser()
    if request.method == 'POST' :
        form= NewUser(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return res(request)
        else :
            print(' Error validation')
    return render(request,'user.html',{'form':form})

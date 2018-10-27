from django.shortcuts import render

def index(request):
    my_dict = {'name':"my world" , 'date':99}
    return render(request,'index.html', context=my_dict)
def other(request):
    return render(request,'other.html')
def relative_url_template(request):
    return render(request, 'relative_url_template.html')

# Create your views here.

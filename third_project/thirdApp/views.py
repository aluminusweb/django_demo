from django.shortcuts import render
from . import Form
def index(request):
    return render(request,"index.html")

def form_name(request):
    dict={"form":Form.FormName()}
    if request.method=='POST':
        form = Form.FormName(request.POST)
        if form.is_valid():
            print("Validation Succesful")
            print("Name :"+ form.cleaned_data['name'])
            print("Email :"+ form.cleaned_data['email'])
            print("Text :"+ form.cleaned_data['text'])

    return render(request,"Form_Name.html", context =dict)

# Create your views here.

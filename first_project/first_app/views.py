from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import Topic,AccessRecord,WebPage
def index(request):
    webpages_list=AccessRecord.objects.order_by('date')
    webDict={"access_record":webpages_list}
    #my_dict={"insert_me":"I am the Developer"}
    return render(request,'index.html',context=webDict)
# Create your views here.

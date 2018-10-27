import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','first_project.settings')
import django
django.setup()
import random
from first_app.models import Topic,AccessRecord,WebPage
from faker import Faker
fakergen=Faker()
Topics=["Ram","Shyam","Anuj","Aryan","Himanshu"]
def add_topic():
    topi=Topic.objects.get_or_create(topic_name=random.choice(Topics))[0]
    topi.save()
    return topi
def populate_tab(N=5):
    top=add_topic()
    fake_name=fakergen.company()
    fake_url=fakergen.url()
    fake_date=fakergen.date()
    for i in range(0,N):
        web=WebPage.objects.get_or_create(topic=top,name=fake_name,url=fake_url)[0]
        print(web)
        web.save()
        AccessRecord.objects.get_or_create(name=web,date=fake_date)
if __name__=='__main__':
    print("Populate started")
    populate_tab(N=50)
    print("populate completed")

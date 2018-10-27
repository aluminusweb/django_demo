import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE","second_project.settings")
import django
django.setup()
from secondApp.models import Intro
from faker import Faker
fakergen = Faker()
def populate_me(N=5):
    for acc in range(0,5):

         str_name = fakergen.name()
         fake_name = str_name.split(' ',2)[0]
         fake_last= str_name.split(' ',2)[1]
         fake_email=fakergen.email()
         Intro.objects.get_or_create(first_name=fake_name,last_name=fake_last,email=fake_email)

if __name__=="__main__":
    print("populating")
    populate_me(N=50)
    print("Completed")

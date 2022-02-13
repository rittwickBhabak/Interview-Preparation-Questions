import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')

import django
django.setup()

from posts.models import Post
from faker import Faker
import random

fakegen = Faker()

def populate(N=10):

    for entry in range(N):

        fake_title = fakegen.name()
        
        fake_description = ''
        no_of_sen = random.randint(20,50)
        for i in range(no_of_sen):
            fake_description = fake_description + ' ' + fakegen.sentence()

        # New entry
        Post.objects.create(title=fake_title, body=fake_description)


if __name__ == "__main__":
    print('Populating...')
    populate(30)
    print('Complete!')
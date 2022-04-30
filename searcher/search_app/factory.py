# factories.py
import factory
from factory.django import DjangoModelFactory
import pytz
from datetime import timedelta as delta
import random

tz = pytz.timezone('Africa/Lagos')
td = delta(days=10)


from .models import Post

class PostFactory(DjangoModelFactory):
    class Meta:
        model = Post

    title = factory.Faker('text', max_nb_chars=50)
    description = factory.Faker('text', max_nb_chars=200)
    body = factory.Faker('paragraph', nb_sentences=50, variable_nb_sentences=False)
    created = factory.Faker('date_time', tzinfo=tz)
    updated = factory.Faker('date_time_between', tzinfo=tz, start_date=td)

    
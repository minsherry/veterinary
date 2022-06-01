import random
from secrets import choice
import pytz
from datetime import datetime
from django.utils import timezone
from faker import Faker
from scipy import rand
from app0.models import *

faker = Faker('zh-TW')
print("產生 美容紀錄")

#檢查寵物
pets = Pet.objects.all()
groomers = Employee.objects.filter(job = 2)
assistants = Employee.objects.filter(job = 3)
gromming_items = GroomingItem.objects.all()
if pets.count() == 0:
    print("沒有寵物")

elif groomers.count() == 0:
    print("沒有獸醫")

else:
    tz = pytz.timezone('Asia/Taipei')
    for i in range(10):
        dt = tz.localize(faker.date_time(), is_dst = True)
        m = PetGroomingRecord.objects.create(
            record_datetime = dt,
            spend_time_in_minute = random.randint(1,800),
            pet = random.choice(pets),
            groomer = random.choice(groomers),
            detail = faker.texts(nb_texts = 3),
        )

        if assistants.count() > 0:
            for i in range(random.randint(0, assistants.count())):
                m.assistant.add(random.choice(assistants))

        if gromming_items.count() > 0:
            for i in range(random.randint(0, gromming_items.count())):
                m.gromming_item.add(random.choice(gromming_items))
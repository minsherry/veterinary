import random
import pytz
from datetime import datetime
from django.utils import timezone
from faker import Faker
from app0.models import *

faker = Faker('zh-TW')
print("產生 預約 戰不可用")

#檢查寵物
pets = Pet.objects.all()
hospitals = Hospital.objects.all()
if pets.count() == 0:
    print("沒有寵物")

elif hospitals.count() == 0:
    print("沒有醫院")

else:
    tz = pytz.timezone('Asia/Taipei')
    for i in range(1):
        dt = tz.localize(faker.date_time(), is_dst = True)
        Reserve.objects.create(
            reserve_datetime = dt,
            pet_id = random.randint(1, pets.count()),
            purpose = random.randint(0, 1),
            hospital_id = random.randint(1, hospitals.count()),
        )
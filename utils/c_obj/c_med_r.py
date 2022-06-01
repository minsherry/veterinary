import random
from secrets import choice
import pytz
from datetime import datetime
from django.utils import timezone
from faker import Faker
from scipy import rand
from app0.models import *

faker = Faker('zh-TW')
print("產生 醫療紀錄")

#檢查寵物
pets = Pet.objects.all()
veterinarys = Employee.objects.filter(job = 0)
assistants = Employee.objects.filter(job = 1)
medical_items = MedicalItem.objects.all()
if pets.count() == 0:
    print("沒有寵物")

elif veterinarys.count() == 0:
    print("沒有獸醫")

else:
    tz = pytz.timezone('Asia/Taipei')
    for i in range(1):
        dt = tz.localize(faker.date_time(), is_dst = True)
        m = MedicalRecord.objects.create(
            record_datetime = dt,
            spend_time_in_minute = random.randint(1,800),
            pet = random.choice(pets),
            veterinary = random.choice(veterinarys),
            detail = faker.texts(nb_texts = 3),
        )

        if assistants.count() > 0:
            for i in range(random.randint(0, assistants.count())):
                m.assistant.add(random.choice(assistants))

        if medical_items.count() > 0:
            for i in range(random.randint(0, medical_items.count())):
                m.medical_item.add(random.choice(medical_items))
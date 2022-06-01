import random
from datetime import datetime
from faker import Faker
from app0.models import *

faker = Faker('zh-TW')

print("產生 合約")

hospitals = Hospital.objects.all()
employees = Employee.objects.all()
if employees.count() == 0:
    print("沒有雇員")

elif hospitals.count() == 0:
    print("沒有醫院")

else:
    for e in employees:
        start_date = datetime.datetime.strptime(faker.date(), "%Y-%m-%d")
        Contract.objects.create(
            sign_date = start_date,
            end_date = start_date + datetime.timedelta(days = 360),
            hospital_id = random.randint(1, hospitals.count()),
            employee = e,
        )
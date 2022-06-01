import random
from datetime import datetime
from faker import Faker
from app0.models import *

faker = Faker('zh-TW')

print("建造 員工")

for i in range(30):
    ph_no=[]
    ph_no.append(0)
    ph_no.append(9)
    for i in range(8):
        ph_no.append(random.randint(0,9))
    ph = ''.join(str(e) for e in ph_no)

    Employee.objects.create(
        first_name = faker.first_name(),
        last_name = faker.last_name(),
        phone = ph,
        birth_date = datetime.datetime.strptime(faker.date(), "%Y-%m-%d"),   
        address = faker.address(),
        email = faker.ascii_free_email(),
        job = random.randint(0, 3),
    )
import random
from datetime import datetime
from faker import Faker
from app0.models import *

faker = Faker('zh-TW')

print("建造 顧客(主人)")

for i in range(10):
    ph_no=[]
    ph_no.append(0)
    ph_no.append(9)
    for i in range(8):
        ph_no.append(random.randint(0,9))
    ph = ''.join(str(e) for e in ph_no)

    Owner.objects.create(
        first_name = faker.first_name(),
        last_name = faker.last_name(),
        birth_date = datetime.datetime.strptime(faker.date(), "%Y-%m-%d"),
        phone = ph,
        email = faker.ascii_free_email(),
        address = faker.address()
    )
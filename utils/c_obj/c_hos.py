import random
from datetime import datetime
from faker import Faker
from app0.models import *

faker = Faker('zh-TW')

print("建造 醫院")
  
for i in range(10):
    # ph_no=[]
    # ph_no.append(0)
    # ph_no.append(9)
    # for i in range(8):
    #     ph_no.append(random.randint(0,9))
    # ph = ''.join(str(e) for e in ph_no)

    Hospital.objects.create(
        name = faker.company_prefix(),
        address = faker.address(),
    )
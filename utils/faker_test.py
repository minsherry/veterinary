from datetime import datetime
import random
from faker import Faker
from app0.models import *

faker = Faker('zh-TW')

print(faker.first_name())
print(faker.last_name())
print(faker.date())
print(type(faker.date()))
ph_no=[]
ph_no.append(0)
ph_no.append(9)
for i in range(8):
    ph_no.append(random.randint(0,9))
ph = ''.join(str(e) for e in ph_no)
print(ph)
print(faker.ascii_free_email())
print(faker.address())
print(faker.date())
print(type(faker.date()))
print(faker.date_time())
print(type(faker.date_time()))
# a = datetime.datetime.strptime(faker.date_time(), "%Y-%m-%d %h:%M:%S")
# print(type(a))

# for i in range(10):
#     ph_no=[]
#     ph_no.append(0)
#     ph_no.append(9)
#     for i in range(8):
#         ph_no.append(random.randint(0,9))
#     ph = ''.join(str(e) for e in ph_no)
#     Customer.objects.create(
#         first_name = faker.first_name(),
#         last_name = faker.last_name(),
#         birth_date = datetime.strptime(faker.date(), "%Y-%m-%d"),
#         phone = ph,
#         email = faker.ascii_free_email(),
#         address = faker.address()
#     )

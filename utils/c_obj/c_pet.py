import random
from datetime import datetime
from faker import Faker
from app0.models import *

faker = Faker('zh-TW')

print("建造 寵物")

#判斷主人
owner_cnt = Owner.objects.all().count()
if owner_cnt == 0:
    print('沒有主人')
else:
    while True:
        id = random.randint(1,owner_cnt)
        try:
            owner = Owner.objects.get(id = id)
            break
        except:
            pass
    print('找到主人')

    for i in range(20):
        # ph_no=[]
        # ph_no.append(0)
        # ph_no.append(9)
        # for i in range(8):
        #     ph_no.append(random.randint(0,9))
        # ph = ''.join(str(e) for e in ph_no)

        Pet.objects.create(
            name = faker.name(),
            nickname = faker.name(),
            owner_id = random.randint(1, owner_cnt),
            gender = random.randint(0, 1),
            birth_date = datetime.datetime.strptime(faker.date(), "%Y-%m-%d"),
            species = faker.last_name(),
        )
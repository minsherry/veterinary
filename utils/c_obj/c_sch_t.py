import random
from datetime import datetime
from faker import Faker
from app0.models import *

faker = Faker('zh-TW')

print("產生 時程表")

for i in range(100):
    clock0 = random.randint(0,23)
    minute0 = random.randint(0,59)
    clock1 = random.randint(0,23)
    minute1 = random.randint(0,59)
    ScheduleTime.objects.create(
        start_work = '%02d%02d' %(clock0, minute0),
        get_off = '%02d%02d' %(clock1, minute1),
    )
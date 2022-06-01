import random
from datetime import datetime
from faker import Faker
from app0.models import *

faker = Faker('zh-TW')

print("排班")
schedule_times = ScheduleTime.objects.all()
employees = Employee.objects.all()
if schedule_times.count() == 0:
    print('沒有時程表')
elif employees.count() == 0:
    print('沒有員工')
else:

    for i in range(100):

        Schedule.objects.create(
            work_date = datetime.datetime.strptime(faker.date(), "%Y-%m-%d"),
            schedule_time = random.choice(schedule_times),
            employee = random.choice(employees),
        )
import random
from datetime import datetime
from faker import Faker
from app0.models import *

faker = Faker('zh-TW')

print("產生 美容項目")

for i in range(20):
    GroomingItem.objects.create(
        name = faker.word(),
        fee = random.randint(100, 100000),
        symptom = faker.texts(nb_texts = 1),
    )
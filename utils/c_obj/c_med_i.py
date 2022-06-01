import random
from datetime import datetime
from faker import Faker
from app0.models import *

faker = Faker('zh-TW')

print("產生 醫療項目")

for i in range(20):
    MedicalItem.objects.create(
        name = faker.word(),
        fee = random.randint(100, 100000),
        symptom = faker.texts(nb_texts = 3),
    )
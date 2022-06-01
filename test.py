from testapp.models import *
all = Combo.objects.all()
for c in all:
    print(c.food.name)
from rest_framework import serializers

from .models import *

class FoodSerializer(serializers.ModelSerializer):
    # name = serializers.CharField()
    # number = serializers.IntegerField()
    class Meta:
        model = Food
        fields = '__all__'

# foodd = FoodSerializer()


class TestSerializer(serializers.ModelSerializer):
    # food = FoodSerializer() #many = True
    # cost = serializers.IntegerField()
    # food_name = serializers.RelatedField(source = 'food', read_only=True)
    food = FoodSerializer()
    class Meta:
        model = Combo
        fields = '__all__'

    def __unicode__(self):
        return self.name
    
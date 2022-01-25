from rest_framework import serializers
from Main.models import Player



class PlayerListSerializers(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = ('id', 'name', 'race')


class PlayerDetailSerializers(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = Player
        fields = '__all__'


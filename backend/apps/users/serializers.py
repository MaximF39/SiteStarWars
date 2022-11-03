from rest_framework import serializers
from users.models import User



class PlayerListSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'name', 'race')


class PlayerDetailSerializers(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = User
        fields = '__all__'


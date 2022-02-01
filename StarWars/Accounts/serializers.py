from rest_framework import serializers
from Accounts.models import MyUser



class PlayerListSerializers(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        fields = ('id', 'name', 'race')


class PlayerDetailSerializers(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = MyUser
        fields = '__all__'


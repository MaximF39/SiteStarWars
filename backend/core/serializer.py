from rest_framework import serializers


class CoreSerializer(serializers.ModelSerializer):

    class Meta:
        exclude = ['created_at', 'updated_at']

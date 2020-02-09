from django.contrib.auth.models import User, Group
from rest_framework import serializers

from bookmymovie.app.models import Screen, SeatInfo


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class SeatInfoSerializer(serializers.ModelSerializer):

    class Meta:
        model = SeatInfo
        fields = ['row', 'num_seats', 'aisle_seats']


class ScreenSerializer(serializers.ModelSerializer):
    seat_info = SeatInfoSerializer(many=True, read_only=False)

    class Meta:
        model = Screen
        fields = ['id', 'name', 'seat_info']

    def create(self, validated_data):
        seat_info = validated_data.pop('seat_info')
        screen = Screen.objects.create(**validated_data)
        for info in seat_info:
            print(info)
            SeatInfo.objects.create(screen=screen, **info)
        return screen


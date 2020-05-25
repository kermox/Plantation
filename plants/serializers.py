from django.contrib.auth import get_user_model
from rest_framework import serializers


from .models import Category, Plant, Room, UserPlant


class AdminCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = [
            'id',
            'name',
            'description',
            'user',
            'slug',
            'image_url',
            'url',
        ]
        lookup_field = 'slug'
        extra_kwargs = {
            'url': {
                'lookup_field': 'slug'
            }
        }


class CategorySerializer(AdminCategorySerializer):
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )


class AdminPlantSerializer(serializers.ModelSerializer):

    class Meta:
        model = Plant
        fields = [
            'id',
            'name',
            'description',
            'category',
            'watering_interval',
            'fertilizing_interval',
            'required_exposure',
            'required_humidity',
            'required_temperature',
            'blooming',
            'difficulty',
            'user',
            'url',

        ]


class PlantSerializer(AdminPlantSerializer):
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )


class AdminRoomSerializer(serializers.ModelSerializer):

    class Meta:
        model = Room
        fields = [
            'id',
            'name',
            'description',
            'exposure',
            'humidity',
            'temperature',
            'drafty',
            'user',
            'url',

        ]


class RoomSerializer(AdminRoomSerializer):
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )


class AdminUserPlantSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserPlant
        fields = [
            'id',
            'name',
            'description',
            'room',
            'plant',
            'last_watered',
            'last_fertilized',
            'image_url',
            'user',
            'url',

        ]


class UserPlantSerializer(AdminUserPlantSerializer):
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = [
            'id',
            'username',
            'email',
            'password',

        ]

from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class meta:
        model = User
        Fields = (
            'first_name',
            'last_name',
            'phone_number',
            'password',
            'email',
            )
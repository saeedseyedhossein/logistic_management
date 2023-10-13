from rest_framework import serializers
from api.models import Company
import hashlib
import re
from django.core.exceptions import ValidationError

def validate_password(value):
    if len(value) < 6:
        raise ValidationError("Password must be at least 6 characters long.")

    if not re.match(r"^(?=.*[a-z])(?=.*[A-Z])[\w\d ]+$", value):
        raise ValidationError(
            "Password must contain at least one lowercase letter, one uppercase letter, and only letters, space, and numbers are allowed."
        )
    
class CompanySerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, validators=[validate_password])

    class Meta:
        model = Company
        fields = ['username', 'password']
        extra_kwargs = {
            'password' : {'write_only':True}
        }

    def create(self, validated_data):
        password = None
        password = validated_data.get('password')
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.password = hashlib.md5(password.encode()).hexdigest()
        instance.save()
        return instance



 
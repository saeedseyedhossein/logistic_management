from rest_framework import serializers
from api.models import Company
import hashlib
class CompanySerializer(serializers.ModelSerializer):
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



 
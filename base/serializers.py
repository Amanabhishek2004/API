from rest_framework import serializers
from .models import *



class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = "__all__" 

class AdvocateSerializer(serializers.ModelSerializer):
    company = CompanySerializer()
    class Meta :
        model = Advocate
        fields = "__all__"
        
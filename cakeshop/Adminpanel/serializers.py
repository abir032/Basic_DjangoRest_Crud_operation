from rest_framework import serializers
from Adminpanel.models import adminpanel




class adminserializer(serializers.ModelSerializer):
    class Meta: 
        model = adminpanel
        fields = '__all__'

from rest_framework import serializers
from .models import Projects, Tasks, Profile

class ProjectsSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Projects
        fields = "__all__"

class TaskViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tasks        
        fields = '__all__'
class ProfileViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'
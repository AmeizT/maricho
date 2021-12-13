from django.db.models import fields
from apps.posts.models import Post, Tech
from rest_framework import serializers
from apps.users.models import User

class TechSerializer(serializers.ModelSerializer): 
    class Meta:
        model = Tech
        fields = '__all__'
class PostSerializer(serializers.ModelSerializer):
    tech = TechSerializer(many=True)
    class Meta:
        model = Post
        fields = ('id', 'author', 'title', 'description', 'location', 'compensation', 'currency', 'interval', 'industry', 'experience', 'tech', 'workplace', 'mode', 'benefits', 'slug', 'created', 'updated',)
        depth = 1
        

from django.db.models import fields
from apps.posts.models import Post
from rest_framework import serializers
from apps.users.models import User

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'


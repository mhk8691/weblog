from rest_framework import serializers
from Categories.models import Category


class PostSerializer(serializers.Serializer):
    id = serializers.IntegerField()

    title = serializers.CharField(max_length=200)
    content = serializers.CharField(max_length=200)
    image = serializers.ImageField()
    is_draft = serializers.BooleanField(default=True)

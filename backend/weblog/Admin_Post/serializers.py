from rest_framework import serializers
from Blog.models import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = (
            "id",
            "author",
            "title",
            "content",
            "is_draft",
            "categories",
        )

    author = serializers.CharField(source="author.username", read_only=True)
    categories = serializers.CharField(source="categories.name", read_only=True)

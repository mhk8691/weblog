from rest_framework import serializers
from Blog.models import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = (
            # "post_id",
            "author",
            "title",
            "content",
            "is_draft",
            "categories",
        )

    author = serializers.CharField(source="author.username", read_only=True)

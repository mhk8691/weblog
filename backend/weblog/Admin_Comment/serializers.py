from rest_framework import serializers
from User.models import Comment


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = (
            "id",
            "author",
            "content",
            "post",
        )

    author = serializers.CharField(source="author.username", read_only=True)
    post = serializers.CharField(source="post.title", read_only=True)

from django.http import JsonResponse
from Blog.models import Post
from .serializers import CommentSerializer
import json

from rest_framework.decorators import api_view
from rest_framework.response import Response
from User.models import User
from Categories.models import Category
from User.models import Comment


@api_view(["GET"])
def list_comment(request):
    # if request.method == "GET":
    #     comment = Comment.objects.all()
    #     serialize = CommentSerializer(comment, many=True)
    #     response = serialize.data
    #     # response.headers["Access-Control-Expose-Headers"] = "Content-Range"
    #     # response.headers["Content-Range"] = len(Comment)
    #     return Response(response)
    range = request.GET["range"]
    sort = request.GET["sort"]
    final_range = json.loads(range)
    final_sort = json.loads(sort)
    if final_sort[1] == "DESC":
        comments = Comment.objects.all().order_by("-{}".format(final_sort[0]))[
            final_range[0] : final_range[1]
        ]
    else:
        comments = Comment.objects.all().order_by(final_sort[0])[
            final_range[0] : final_range[1]
        ]
    serializer = CommentSerializer(comments, many=True)
    response = Response(serializer.data)
    response["Content-Range"] = f"comments 0-{len(comments)-1}/{len(comments)}"
    response["Access-Control-Expose-Headers"] = "Content-Range"
    return response


def get_comment(comment_id):
    comment = Comment.objects.get(id=comment_id)
    serializer = CommentSerializer(comment)
    return serializer.data


@api_view(["POST"])
def add_comment(request):
    if request.method == "POST":
        json_data = json.loads(request.body)
        author = json_data.get("author")
        comment = json_data.get("comment")
        post = json_data.get("post")
        user = User.objects.get(pk=author)
        post = Post.objects.get(pk=post)
        comment = Comment.objects.create(
            author=user,
            content=comment,
            post=post,
        )
        final_comment = get_comment(comment.pk)
        print(final_comment)
        return Response(final_comment)


@api_view(["DELETE", "GET", "PUT"])
def crud(request, comment_id):
    comment = Comment.objects.get(pk=comment_id)

    if request.method == "GET":
        getComment = get_comment(comment_id=comment_id)

        return Response(getComment)
    elif request.method == "DELETE":
        try:
            comment.delete()
            return Response({"id": comment_id})
        except Comment.DoesNotExist:
            return JsonResponse({"error": "User not found"})
    elif request.method == "PUT":
        serializer = CommentSerializer(comment, data=request.data)
        if serializer.is_valid():
            serializer.save()

            return Response(get_comment(comment_id))
        else:
            return Response(serializer.errors)
            # response = JsonResponse(get_user(user_id), safe=False)

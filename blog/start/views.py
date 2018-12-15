from rest_framework import viewsets
from blog.start.serializers import PostSerializer
# from blog.blog_api.serializers import DetailSerializer
from blog.models import Post
# from blog.permissions import IsOwnerOrReadOnly


# mixin classes provide the .list() and .create() actions
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


# class DetailViewSet(viewsets.ModelViewSet):
#     queryset = Post.objects.all()
#     serializer_class = DetailSerializer
#
#

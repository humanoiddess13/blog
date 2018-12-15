from rest_framework import serializers
from blog.models import Post


# from django.contrib.auth.models import Post


class PostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:  # vew' otnositsya k model'ke ili k atributu
        model = Post
        fields = ('title', 'text', 'published_date')

#
# class DetailSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Post
#         fields = ( 'title', 'text')

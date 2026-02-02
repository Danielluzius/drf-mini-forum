from rest_framework import serializers
from forum_app.models import Post, Comment


class PostSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    
    class Meta:
        model = Post
        fields = ['id', 'title', 'content', 'author', 'created_at']
        read_only_fields = ['created_at']


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    
    class Meta:
        model = Comment
        fields = ['id', 'post', 'text', 'author', 'created_at']
        read_only_fields = ['created_at']
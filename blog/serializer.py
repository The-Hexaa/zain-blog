from .models import *
from rest_framework import serializers
from django.db.models import Count
from django.conf import settings

class PostSerializer(serializers.ModelSerializer):
    likes_count = serializers.SerializerMethodField()
    comments_count = serializers.SerializerMethodField()

    def get_likes_count(self, post):
        return Like.objects.filter(post=post, status='like').count()
    
    def get_comments_count(self, post):
        return Comment.objects.filter(post=post).count()

    class Meta:
        model = Post
        fields = "__all__"


        
class RecursiveCommentSerializer(serializers.ModelSerializer):
    likes_count = serializers.SerializerMethodField()
    user_name = serializers.SerializerMethodField()

    def get_likes_count(self, comment):
        return Like.objects.filter(comment=comment).count()

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        if self.context.get('depth', 0) <= 0:
            return representation
        representation['replies'] = self.get_replies(instance)
        return representation
    
    def get_user_name(self, comment):
        return comment.user.name if comment.user else None

    def get_replies(self, obj):
        replies = Comment.objects.filter(parent_comment=obj)
        if self.context.get('depth', 0) <= 1:
            return []
        serializer = RecursiveCommentSerializer(replies, many=True, context=self.context)
        return serializer.data
    
    

    class Meta:
        model = Comment
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    likes_count = serializers.SerializerMethodField()
    replies = RecursiveCommentSerializer(many=True, read_only=True)
    user_name = serializers.SerializerMethodField()


    def get_likes_count(self, comment):
        return Like.objects.filter(comment=comment).count()
    
    def get_user_name(self, comment):
        return comment.user.name if comment.user else None
    
    class Meta:
        model = Comment
        fields = "__all__"
        
class TagSerializer(serializers.ModelSerializer):
    posts_count = serializers.SerializerMethodField()
    
    def get_posts_count(self, tag):
        return Post.objects.filter(tag=tag).count()
    class Meta:
        model = Tag
        fields= "__all__"

class CategorySerializer(serializers.ModelSerializer):
    posts_count = serializers.SerializerMethodField()
    
    def get_posts_count(self, category):
        return Post.objects.filter(category=category).count()
    
    class Meta:
        model = Category
        fields= "__all__"

class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields= "__all__"
        

class FirstPostIdSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id']



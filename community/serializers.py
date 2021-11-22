from rest_framework import serializers
from .models import Article, Comment


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ('id', 'title', 'content', 'created_at', 'updated_at', 'user_id',)

class CommentSerializer(serializers.ModelSerializer):
    # article = ArticleSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = ('id', 'content', 'user_id', )
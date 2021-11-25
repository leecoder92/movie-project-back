from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ArticleSerializer, CommentSerializer
from rest_framework import status
from .models import Article, Comment


@api_view(['GET', 'POST'])
def article_create(request):
    if request.method == "GET":
        articles = Article.objects.order_by('-pk')
        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data)

    elif request.method == "POST":
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['PUT', 'DELETE'])
def article_update_delete(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)

    if not request.user.article_set.filter(pk=article_pk).exists():
        return Response({'detail': '권한이 없습니다.'}, status=status.HTTP_403_FORBIDDEN)

    if request.method == 'PUT':
        serializer = ArticleSerializer(article, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user)
            return Response(serializer.data)

    elif request.method == 'DELETE':
        article.delete()
        return Response({ 'id': article_pk }, status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def comment_list_create(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    
    if request.method == "GET":
        comments = article.comment_set.all()
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)

    elif request.method == "POST":
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(article=article, user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['DELETE'])
def comment_delete(request, article_pk, comment_pk):
    # article = get_object_or_404(Article, pk=article_pk)
    comment = get_object_or_404(Comment, pk=comment_pk)

    if not request.user.comment_set.filter(pk=comment_pk).exists():
        return Response({'detail': '권한이 없습니다.'}, status=status.HTTP_403_FORBIDDEN)

    if request.method == 'DELETE':
        comment.delete()
        return Response({ 'id': comment_pk }, status=status.HTTP_204_NO_CONTENT)

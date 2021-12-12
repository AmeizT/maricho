from apps.posts.models import Post
from rest_framework.response import Response
from rest_framework import permissions, status, views, viewsets
from .serializers import PostSerializer
from rest_framework.decorators import api_view
from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import api_view, permission_classes


class NewsFeedView(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.AllowAny]
    lookup_field = 'slug'

    
@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def add_bookmarks(request, id, *args, **kwargs):
    product = get_object_or_404(Post, id=id)
    if product.saved.filter(id=request.user.id).exists():
        product.saved.remove(request.user)
        return Response({'response': 'removed'})
    else:
        product.saved.add(request.user)
        return Response({'response': 'added'})
    
    return Response({'response': 'Added to bookmarks'}, status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_bookmarks(request):
    product = Post.objects.filter(saved=request.user).order_by('user_bookmarks')
    serializer = PostSerializer(product, many=True)
    return Response(serializer.data)


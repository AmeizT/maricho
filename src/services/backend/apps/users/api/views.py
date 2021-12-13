import json
from rest_framework import status
from apps.users.models import User
from requests import Request, Session
from rest_framework import permissions
from .serializers import UserSerializer
from rest_framework import views, viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import api_view, permission_classes
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
from django.http import HttpResponse

# class AdminBrowsableMixin(object):
#     def get_renderers(self):
#         # rends = self.renderer_classes
#         # if self.request.user and self.request.user.is_admin:
#         #     rends.append(renderers.BrowsableAPIRenderer)
#         # return [renderer() for renderer in rends]
#         return Response('hello')


class UserView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'username'

    # def get_permissions(self):
    #     if self.action == 'list':
    #         permission_classes = [permissions.IsAdminUser]
    #     else:
    #         permission_classes = [permissions.IsAuthenticated]
    #     return [permission() for permission in permission_classes]

    # def post(self, request):
    #     serializer = UserSerializer(data=request.data)
    #     if serializer.is_valid():
    #         user = serializer.save()
    #         if user:
    #             return Response({'message': 'created'}, status=status.HTTP_201_CREATED)
    #         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def unauthorized(request):
    return HttpResponse('Well tried Joe but you are not authorized to view this page')


@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def bookmarks_add_view(request, id, *args, **kwargs):
    product = get_object_or_404(Product, id=id)
    if product.saved.filter(id=request.user.id).exists():
        product.saved.remove(request.user)
        return Response({'response': 'removed'})
    else:
        product.saved.add(request.user)
        return Response({'response': 'added'})

    return Response({'response': 'Added to bookmarks'}, status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def list_bookmarks(request):
    product = Product.objects.filter(
        saved=request.user).order_by('user_bookmarks')
    serializer = ProductSerializer(product, many=True)
    return Response(serializer.data)


@api_view(('GET',))
def user_location(requests):
    url = 'http://ipinfo.io?token=481400e61b9a2c'
    headers = {
        'Accepts': 'application/json',
    }

    session = Session()
    session.headers.update(headers)

    try:
        response = session.get(url)
        data = json.loads(response.text)
        return Response(data, status=status.HTTP_200_OK)
    except (ConnectionError, Timeout, TooManyRedirects) as e:
        return Response({'message': 'User location set failed'}, status=status.HTTP_404_NOT_FOUND)








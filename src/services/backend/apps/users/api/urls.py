from django.conf import settings
from django.urls import path, include
from rest_framework import urlpatterns
from rest_framework.routers import DefaultRouter, SimpleRouter
from .views import UserView, bookmarks_add_view, list_bookmarks, user_location

# if settings.DEBUG:
#     router = DefaultRouter()
# else:
#     router = SimpleRouter()

router = DefaultRouter()
router.register('users', UserView, basename="user")
urlpatterns = router.urls

urlpatterns = [
    path('', include(router.urls)),
    path('users/me/bookmarks/<int:id>/', bookmarks_add_view),
    path('users/me/bookmarks/', list_bookmarks),
    path('users/me/location/', user_location),
]

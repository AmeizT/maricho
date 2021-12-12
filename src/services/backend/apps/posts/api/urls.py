from django.urls import path
from django.urls.conf import include
from rest_framework.routers import DefaultRouter
from .views import NewsFeedView

router = DefaultRouter()
router.register('feed', NewsFeedView, basename='feed')
urlpatterns = router.urls

urlpatterns = [
    path('', include(router.urls)),
]

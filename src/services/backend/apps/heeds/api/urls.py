from django.urls import path
from django.urls.conf import include
from rest_framework.routers import DefaultRouter
from .views import HeedView

router = DefaultRouter()
router.register('heed', HeedView, basename='heed')
urlpatterns = router.urls

urlpatterns = [
    path('', include(router.urls)),
]

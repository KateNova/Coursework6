from rest_framework import routers

from .views import CommentViewSet, AdViewSet

router = routers.DefaultRouter()
router.register('ads', AdViewSet, basename='ad')
router.register(
    r'ads/(?P<ad_id>\d+)/comments',
    CommentViewSet,
    basename='comment'
)

urlpatterns = []
urlpatterns += router.urls

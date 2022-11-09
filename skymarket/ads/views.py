from django.shortcuts import get_object_or_404
from rest_framework import pagination, viewsets
from rest_framework.decorators import action
from rest_framework.filters import SearchFilter

from .models import Ad, Comment
from .permissions import AdUpdateDeletePermission
from .serializers import AdSerializer, AdDetailSerializer, CommentSerializer


class AdPagination(pagination.PageNumberPagination):
    page_size = 10


class AdViewSet(viewsets.ModelViewSet):
    permission_classes = (AdUpdateDeletePermission, )
    pagination_class = AdPagination
    filter_backends = (SearchFilter, )
    search_fields = ('title', )

    def get_queryset(self):
        if self.action == 'me':
            return self.request.user.ads.all()
        return Ad.objects.all()

    @action(['get'], detail=False, name='me')
    def me(self, request, *args, **kwargs):
        if self.request.method == 'GET':
            return self.list(request, *args, **kwargs)

    def get_serializer_class(self):
        if self.action == 'list':
            return AdSerializer
        return AdDetailSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    pagination_class = AdPagination

    def get_ad(self):
        return get_object_or_404(Ad, pk=self.kwargs['ad_id'])

    def get_queryset(self):
        return Comment.objects.filter(ad=self.get_ad())

    def perform_create(self, serializer):
        serializer.save(
            ad=self.get_ad(),
            author=self.request.user
        )

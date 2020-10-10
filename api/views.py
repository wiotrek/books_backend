from .models import Book
from .serializers import BookSerializer, BookDetailsSerializer, BookPostSerializer
from rest_framework.response import Response
from rest_framework import viewsets, status
from rest_framework.authentication import TokenAuthentication


class BookViewSet(viewsets.ModelViewSet):
    serializer_class = BookSerializer
    authentication_classes = (TokenAuthentication,)

    def get_queryset(self):
        books = Book.objects.filter(user=self.request.user)
        return books

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = BookDetailsSerializer(instance)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        serializer = BookPostSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = BookPostSerializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)

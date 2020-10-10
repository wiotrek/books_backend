from rest_framework import serializers
from .models import Book


class BookSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Book
        fields = ['user', 'id', 'title', 'year', 'author', 'GENRE']


class ChoicesField(serializers.Field):
    def __init__(self, choices, **kwargs):
        self._choices = choices
        super(ChoicesField, self).__init__(**kwargs)

    def to_representation(self, obj):
        return self._choices[obj]

    def to_internal_value(self, data):
        return getattr(self._choices, data)


class BookDetailsSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    genre = ChoicesField(choices=Book.GENRE)

    class Meta:
        model = Book
        fields = ['user', 'id', 'title', 'description', 'year',
                  'rating', 'genre', 'amount_sites', 'when_addition',
                  'author', 'GENRE']


class BookPostSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Book
        fields = ['user', 'id', 'title', 'description', 'year',
                  'rating', 'genre', 'amount_sites', 'when_addition',
                  'author']

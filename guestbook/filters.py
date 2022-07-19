import django_filters
from .models import Guestbook


class GuestbookFilter(django_filters.FilterSet):
    class Meta:
        model = Guestbook
        fields = {
            'author': ['icontains'],
            'title': ['icontains'],
            'text': ['icontains'],
            'date_create': ['lt', 'gt'],
        }

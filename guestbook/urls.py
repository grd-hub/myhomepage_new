from django.urls import path
from .views import GuestbookDetailview, GuestbookCreateView, GuestbookUpdateView, GuestbookDeleteView,\
    list_entries_final

app_name = 'guestbook'

urlpatterns = [
    path('', list_entries_final, name='list_entries_final'),
    path('guestbook_createview/', GuestbookCreateView.as_view(), name="guestbook_createview"),
    path('update/<slug:slug>/', GuestbookUpdateView.as_view(), name="guestbook_updateview"),
    path('detail/<slug:slug>/', GuestbookDetailview.as_view(), name='guestbook_detailview'),
    path('delete/<slug:slug>/', GuestbookDeleteView.as_view(), name="guestbook_deleteview"),
]

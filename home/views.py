from django.shortcuts import render
from .utils import check_http_header_for_accept_language


def home(request):
    content_language = check_http_header_for_accept_language(request)
    context = {
        'content_language': content_language
    }
    return render(request, 'home/home.html', context)

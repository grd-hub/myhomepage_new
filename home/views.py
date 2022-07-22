from django.shortcuts import render

from .utils import check_http_header_for_accept_language

from .models import *


def home(request):
    content_language = check_http_header_for_accept_language(request)

    info_ger = InformationGerman.objects.first()
    info_eng = InformationEnglish.objects.first()

    context = {
        'content_language': content_language,
        'info_ger': info_ger,
        'info_eng': info_eng,
    }
    return render(request, 'home/home.html', context)

def check_http_header_for_accept_language(request):

    '''
    Extract and process header-data from request.META to set the content language for the view.
    '''

    content_language = 'en'
    if request.META['HTTP_ACCEPT_LANGUAGE']:
        first_split = request.META['HTTP_ACCEPT_LANGUAGE'].split(',')
        final_split = []

        for item in first_split:
            final_split.append(item.split(';'))

        for item in final_split:
            if item[0].lower() == 'de' or item[0].lower() == 'de-de' or item[0].lower() == 'de-li' or\
                    item[0].lower() == 'de-lu' or item[0].lower() == 'de-at' or item[0].lower() == 'de-ch':
                content_language = 'de'

        print('HTTP_ACCEPT_LANGUAGE: ', request.META['HTTP_ACCEPT_LANGUAGE'])
        print(first_split)
        print(final_split)
        print(content_language)

        return content_language
    else:
        return content_language

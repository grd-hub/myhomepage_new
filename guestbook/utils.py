from .filters import GuestbookFilter
from .models import Guestbook
from django.core.paginator import Paginator
import random


def check_order_group(request):
    if request.GET['order_group'] == 'author':
        filtered_guestbook = GuestbookFilter(
            request.GET,
            queryset=Guestbook.objects.all().order_by('author')
        )
        order_radio_button = 'author'
    elif request.GET['order_group'] == 'date_ascending':
        filtered_guestbook = GuestbookFilter(
            request.GET,
            queryset=Guestbook.objects.all().order_by('date_create')
        )
        order_radio_button = 'date_ascending'
    elif request.GET['order_group'] == 'date_descending':
        filtered_guestbook = GuestbookFilter(
            request.GET,
            queryset=Guestbook.objects.all().order_by('-date_create')
        )
        order_radio_button = 'date_descending'
    else:
        filtered_guestbook = GuestbookFilter(
            request.GET,
            queryset=Guestbook.objects.all().order_by('author')
        )
        order_radio_button = 'author'

    return order_radio_button, filtered_guestbook


def check_entries_per_page(request, filtered_guestbook, sum_all_entries):
    if request.GET['entries_per_page'] == '8':
        paginated_filtered_guestbook = Paginator(filtered_guestbook.qs, 8)
        entries_per_page = '8'
    elif request.GET['entries_per_page'] == '16':
        paginated_filtered_guestbook = Paginator(filtered_guestbook.qs, 16)
        entries_per_page = '16'
    elif request.GET['entries_per_page'] == '32':
        paginated_filtered_guestbook = Paginator(filtered_guestbook.qs, 32)
        entries_per_page = '32'
    elif request.GET['entries_per_page'] == '64':
        paginated_filtered_guestbook = Paginator(filtered_guestbook.qs, 64)
        entries_per_page = '64'
    elif request.GET['entries_per_page'] == '---------':
        paginated_filtered_guestbook = Paginator(filtered_guestbook.qs, sum_all_entries)
        entries_per_page = '---------'
    else:
        paginated_filtered_guestbook = Paginator(filtered_guestbook.qs, 8)
        entries_per_page = '8'

    return entries_per_page, paginated_filtered_guestbook


def check_page_view(request):
    if request.GET['view_group'] == 'listview':
        page_view = 'listview'
    elif request.GET['view_group'] == 'mosaicview':
        page_view = 'mosaicview'
    else:
        page_view = 'listview'

    return page_view


def add_fifty():
    author = [
        'Robert N. Charrette', 'Nigel Findley', 'Chris Kubasik', 'Carl Sargent', 'Hans Joachim Alpers', 'Tom Dowd',
        'Nyx Smith', 'Marc Gascoigne', 'Caroline Spector', 'Mel Odom', 'Jak Koke', 'Lisa Smedman', 'Nick Polotta',
        'Stephen Kenson', 'Michael A. Stockpole', 'Jonathan Bond', 'Leo Lukas', 'Markus Heitz', 'Harri Assmann',
        'Ivan Nedic', 'Maike Hallmann', 'Lara Möller', 'André Wiesler', 'Sebastian Schäfer', 'Boris Koch',
        'Christian Riesslegger'
    ]
    title = [
        'Never Deal with a Dragon - Secrets of Power - Volume 1',
        'Choose Your Enemies Carefully - Secrets of Power - Volume 2',
        'Find Your Own Truth - Secrets of Power - Volume 3',
        '2XS - To Excess', 'Changeling', 'Never trust an elf', 'Shadowplay', 'Streets of Blood',
        'Das zerrissene Land (Deutschland in den Schatten 1)', 'Die Augen des Riggers (Deutschland in den Schatten 2)',
        'Die graue Eminenz (Deutschland in den Schatten 3)', "Night's Pawn", 'Striper Assassin', 'Lone Wolf',
        'Fade to Black', 'Nosferatu', 'Burning Bright', 'Who hunts the Hunter', 'House of the Sun', 'Worlds Without End',
        'Just Compensation', 'Black Madonna', 'Preying for Keeps', 'Dead Air', 'The Lucifer Deck', 'Steel Rain',
        'Shadowboxer'
    ]
    text = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et' \
           ' dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip' \
           ' ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu' \
           ' fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt' \
           ' mollit anim id est laborum.'

    write_entry = Guestbook(author='GOD', title='this is GOOOOOD', text='if you read this')
    write_entry.save()


'''
    for entry in range(1):
        new_random_int = random.randint(0, 25)
        new_random_int_2 = random.randint(0, 26)
        write_entry = Guestbook.objects.create(
            author=author[new_random_int],
            title=title[new_random_int_2],
            text=text)
        write_entry.save()
'''
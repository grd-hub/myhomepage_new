from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .filters import GuestbookFilter
from .models import Guestbook

from .utils import check_order_group, check_entries_per_page, check_page_view, add_fifty


class GuestbookDeleteView(DeleteView):
    model = Guestbook
    success_url = reverse_lazy('guestbook:list_entries_final')
    template_name = 'guestbook/guestbook_deleteview.html'


class GuestbookUpdateView(UpdateView):
    model = Guestbook
    fields = [
        'title',
        'text',
    ]
    template_name = 'guestbook/guestbook_updateview.html'
    success_url = '/guestbook/'


class GuestbookCreateView(CreateView):
    model = Guestbook
    fields = [
        'author',
        'title',
        'text',
    ]
    template_name = 'guestbook/guestbook_createview.html'
    success_url = '/guestbook/'


class GuestbookDetailview(DetailView):
    model = Guestbook
    template_name = 'guestbook/guestbook_detailview.html'


def list_entries_final(request):

    if 'add' in request.POST:
        print("I should add 50")
        add_fifty()
        return redirect('guestbook:list_entries_final')



    print()
    print('------------------------------------------------------------')
    print('Request GET data:')
    print(request.GET)
    print()
    print('------------------------------------------------------------')

    if 'order_group' and 'entries_per_page' and 'view_group' in request.GET:

        order_radio_button, filtered_guestbook = check_order_group(request)

        entries = filtered_guestbook.qs
        sum_all_entries = entries.count()

        entries_per_page, paginated_filtered_guestbook = check_entries_per_page(
            request, filtered_guestbook, sum_all_entries
        )

        page_number = request.GET.get('page')
        guestbook_page_obj = paginated_filtered_guestbook.get_page(page_number)
        nums = "a" * guestbook_page_obj.paginator.num_pages

        page_view = check_page_view(request)

        context = {
            'filtered_guestbook': filtered_guestbook,
            'guestbook_page_obj': guestbook_page_obj,
            'nums': nums,
            'order_radio_button': order_radio_button,
            'entries_per_page': entries_per_page,
            'page_view': page_view,
        }
        return render(request, 'guestbook/guestbook_css_grid_final.html', context)

    # DEFAULT RENDERING --> EMPTY GET REQUEST
    else:
        filtered_guestbook = GuestbookFilter(
            request.GET,
            queryset=Guestbook.objects.all().order_by('author')
        )
        paginated_filtered_guestbook = Paginator(filtered_guestbook.qs, 8)
        page_number = request.GET.get('page')
        guestbook_page_obj = paginated_filtered_guestbook.get_page(page_number)
        nums = "a" * guestbook_page_obj.paginator.num_pages

        context = {
            'filtered_guestbook': filtered_guestbook,
            'guestbook_page_obj': guestbook_page_obj,
            'nums': nums,
        }
        return render(request, 'guestbook/guestbook_css_grid_final.html', context)

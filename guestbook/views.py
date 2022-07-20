from django.contrib import messages
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Guestbook
from .filters import GuestbookFilter

from .utils import check_order_group, check_entries_per_page, check_page_view, add_fifty, delete_all_generic_entries


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

        number_of_generic_entries = Guestbook.objects.filter(is_generic=True).count()

        if number_of_generic_entries + 50 >= 101:
            messages.add_message(request, messages.WARNING, 'The maximum are 100 generic entries.')
            return redirect('guestbook:list_entries_final')
        else:
            add_fifty()

    if 'delete' in request.POST:

        delete_all_generic_entries()
        return redirect('guestbook:list_entries_final')

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
            'sum_all_entries': sum_all_entries,
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
        print()
        print('-------------------')
        print(nums)
        print('-------------------')
        print()


        sum_all_entries = Guestbook.objects.count()

        context = {
            'filtered_guestbook': filtered_guestbook,
            'guestbook_page_obj': guestbook_page_obj,
            'nums': nums,
            'sum_all_entries': sum_all_entries
        }
        return render(request, 'guestbook/guestbook_css_grid_final.html', context)

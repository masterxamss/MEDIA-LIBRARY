# from django.shortcuts import render, get_object_or_404
# from django.contrib.auth.decorators import login_required

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView
from library.models import Dvd


class DvdView(LoginRequiredMixin,ListView):
    template_name = "library/dvds/gest_dvds.html"
    model = Dvd
    ordering = ["title"]
    context_object_name = "dvds"
    paginate_by = 10


class DvdDetailView(LoginRequiredMixin, DetailView):
    model = Dvd
    template_name = "library/gest_media.html"
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    context_object_name = 'dvd_detail'


# @login_required
# def LibraryDvdDetailView(request, slug):
#     """
#     Displays the details of a specific Dvd, given its slug.

#     :param request: The request object.
#     :param slug: The slug of the Dvd to be displayed.
#     :return: A rendered template with the Dvd's details.
#     """
#     identified_media = get_object_or_404(Dvd, slug=slug)
#     return render(request, "library/gest_media.html", {
#         "dvd_detail": identified_media
#     })

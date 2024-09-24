# from django.shortcuts import render, get_object_or_404
# from django.contrib.auth.decorators import login_required

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView
from library.models import Cd

class CdView(LoginRequiredMixin,ListView):
    template_name = "library/gest_cds.html"
    model = Cd
    ordering = ["title"]
    context_object_name = "cds"
    paginate_by = 10


class CdDetailView(LoginRequiredMixin, DetailView):
    model = Cd
    template_name = "library/gest_media.html"
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    context_object_name = 'cd_detail'

# @login_required
# def LibraryCdDetailView(request, slug):
#     """
#     Displays the details of a specific Cd, given its slug.

#     :param request: The request object.
#     :param slug: The slug of the Cd to be displayed.
#     :return: A rendered template with the Cd's details.
#     """
#     identified_media = get_object_or_404(Cd, slug=slug)
#     return render(request, "library/gest_media.html", {
#         "cd_detail": identified_media
#     })
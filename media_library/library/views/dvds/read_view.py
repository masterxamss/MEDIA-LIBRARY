# from django.shortcuts import render, get_object_or_404
# from django.contrib.auth.decorators import login_required

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView
from library.models import Dvd


class DvdView(ListView):
    template_name = "library/dvds/gest_dvds.html"
    model = Dvd
    ordering = ["title"]
    context_object_name = "dvds"
    paginate_by = 10

    error = None

    def get_queryset(self):
        """
        Override the default queryset to apply filtering based on the POST request.
        """
        queryset = super().get_queryset()
        
        # Get POST parameters if any
        search_title = self.request.POST.get('search_title','').strip()
        return_availables = self.request.POST.get('return_availables')
        return_unavailables = self.request.POST.get('return_unavailables')

        # Apply filters based on POST data
        if search_title:
            queryset = queryset.filter(title__icontains=search_title)
            if queryset.count() == 0:
                self.error = "Aucun DVD ne correspond à votre recherche."

        if return_availables:
            queryset = queryset.filter(available=True)
            if queryset.count() == 0:
                self.error = "Aucun DVD n'est disponible."

        if return_unavailables:
            queryset = queryset.filter(available=False)
            if queryset.count() == 0:
                self.error = "Aucun DVD n'est indisponible."
                
        return queryset

    
    def get_context_data(self, **kwargs):
        """
        Adds additional context to the response.
        """
        context = super().get_context_data(**kwargs)
        
        # Get total books count
        dvds = Dvd.objects.all()
        context["total"] = dvds.count()
        context["total_availables"] = dvds.filter(available=True).count()
        context["total_unavailables"] = dvds.filter(available=False).count()
        context["error"] = self.error
        context["return_all"] = 'checked' if self.request.POST.get('return_all') else ''
        context["return_availables"] = 'checked' if self.request.POST.get('return_availables') else ''
        context["return_unavailables"] = 'checked' if self.request.POST.get('return_unavailables') else ''
        context["user"] = self.request.user

        return context
        

    def post(self, request, *args, **kwargs):
        """
        Handles the POST request and ensures it triggers the right filtering.
        """
        # Reuse the get method for filtering logic
        return self.get(request, *args, **kwargs)


class DvdDetailView(DetailView):
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

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView
from django.db.models import Q

from library.models import Member

class MembersView(LoginRequiredMixin,ListView):
    template_name = "library/members/gest_members.html"
    model = Member
    ordering = ["last_name"]
    context_object_name = "members"
    paginate_by = 10

    error = None

    def get_queryset(self):

        queryset = super().get_queryset()

        search_name = self.request.POST.get('search_name','').strip()
        return_blocked = self.request.POST.get('return_blocked')

        if search_name:
            queryset = queryset.filter(
                Q(first_name__icontains=search_name) | Q(
                    last_name__icontains=search_name)
            )
            if queryset.count() == 0:
                self.error = "Aucun membre ne correspond à votre recherche."

        if return_blocked:
            queryset = queryset.filter(blocked=True)
            if queryset.count() == 0:
                self.error = "Aucun membre n'est bloqué."

        return queryset


    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)

        members = Member.objects.all()
        context["total"] = members.count()
        context["total_blocked"] = members.filter(blocked=True).count()
        context["error"] = self.error
        context["return_all"] = 'checked' if self.request.POST.get('return_all') else ''
        context["return_blocked"] = 'checked' if self.request.POST.get('return_blocked') else ''

        return context


    def post(self, request, *args, **kwargs):
        """
        Handles a POST request to filter books.

        Reuses the get method for filtering logic.
        """
        return self.get(request, *args, **kwargs)


class MemberDetailView(LoginRequiredMixin, DetailView):
    model = Member
    template_name = "library/gest_media.html"
    pk_url_kwarg = 'id'
    context_object_name = 'member_detail'
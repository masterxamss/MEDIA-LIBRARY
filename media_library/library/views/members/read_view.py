from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView

from library.models import Member

class MembersView(LoginRequiredMixin,ListView):
    template_name = "library/members/gest_members.html"
    model = Member
    ordering = ["last_name"]
    context_object_name = "members"
    paginate_by = 10


class MemberDetailView(LoginRequiredMixin, DetailView):
    model = Member
    template_name = "library/gest_media.html"
    pk_url_kwarg = 'id'
    context_object_name = 'member_detail'
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DeleteView
from library.models import Member


class MemberDeleteView(LoginRequiredMixin, DeleteView):
    model = Member
    template_name = 'library/members/member_confirm_delete.html'
    success_url = reverse_lazy('gest-members')
    pk_url_kwarg = 'id'

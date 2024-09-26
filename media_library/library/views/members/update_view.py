from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import UpdateView

from library.models import Member
from library.forms import MemberForm


class MemberUpdateView(LoginRequiredMixin, UpdateView):
    model = Member
    form_class = MemberForm
    template_name = 'library/members/member_form.html'
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('gest-members')

    def form_valid(self, form):
        return super().form_valid(form)
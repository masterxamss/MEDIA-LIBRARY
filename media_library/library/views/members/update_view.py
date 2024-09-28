from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import UpdateView

from library.models import Member
from library.forms import MemberForm

import logging

logger = logging.getLogger('library')


class MemberUpdateView(LoginRequiredMixin, UpdateView):
    model = Member
    form_class = MemberForm
    template_name = 'library/members/member_form.html'
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('gest-members')

    def form_valid(self, form):
        try:
            logger.info('Update member - USER: %s', self.request.user)
            logger.debug('Member details: %s', form.cleaned_data)
            return super().form_valid(form)
        except Exception as e:
            logger.warning('An error occurred while updating member: %s', str(e))
        return super().form_valid(form)
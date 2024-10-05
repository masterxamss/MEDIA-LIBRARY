from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DeleteView
from library.models import Member

import logging


logger = logging.getLogger('library')


class MemberDeleteView(LoginRequiredMixin, DeleteView):
    model = Member
    template_name = 'library/members/member_confirm_delete.html'
    success_url = reverse_lazy('gest-members')
    pk_url_kwarg = 'id'

    def post(self, request, *args, **kwargs):
        """
        Handles a POST request to delete a member.

        Retrieves the member ID from the URL, gets the member
        object from the database, and calls its delete method. Logs an info
        message with the user and member ID being deleted.

        Args:
            request (HttpRequest): The POST request containing the member ID to delete.
            *args: Additional arguments passed to the function.
            **kwargs: Additional keyword arguments passed to the function.

        Returns:
            HttpResponse: A redirect response to the member list.

        Logs an info message with the user and member ID being deleted.
        Logs an error message with the user and member ID if an error occurs.
        """
        self.object = self.get_object()
        try:
            logger.info('User %s is attempting to delete member ID: %s',
                        self.request.user, self.object.id)
            logger.debug(f'Details member before delete : {self.object}')

            response = self.delete(request, *args, **kwargs)

            logger.info('Member deleted successfully')

            return response

        except Exception as e:
            logger.error('An error occurred while deleting the member: %s',
                         self.object.id, self.request.user, str(e))
            raise

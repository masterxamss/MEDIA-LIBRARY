from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DeleteView
from library.models import Book, MediaReservations
from django.contrib import messages

import logging

logger = logging.getLogger('library')


class BookDeleteView(LoginRequiredMixin, DeleteView):
    model = Book
    template_name = 'library/books/book_confirm_delete.html'
    success_url = reverse_lazy('gest-books')
    slug_field = 'slug'
    slug_url_kwarg = 'slug'

    def post(self, request, *args, **kwargs):
        """
        Handles a POST request to delete a Book.

        Retrieves the Book ID from the URL, gets the Book object from the
        database, and calls its delete method. Logs an info message with the
        user and Book ID being deleted.

        Args:
            request (HttpRequest): The POST request containing the Book ID to delete.
            *args: Additional arguments passed to the function.
            **kwargs: Additional keyword arguments passed to the function.

        Returns:
            HttpResponse: A redirect response to the Book list.

        Logs an info message with the user and Book ID being deleted.
        Logs an error message with the user and Book ID if an error occurs.
        """
        self.object = self.get_object()
        try:
            logger.info('User %s is attempting to delete Book ID: %s',
                        self.request.user, self.object.id)
            logger.debug(f'Details Book before delete : {self.object}')

            active_reservations = MediaReservations.objects.filter(book=self.object, returned=False)

            if active_reservations.exists():
                logger.error('Error deleting Book %s: The Book is present in one or more reservations.',
                            self.object.id)
                messages.error(request, "Ce Livre ne peut pas être annulé. Il y a des emprunts qui n'ont pas encore été retournés.")
                return self.render_to_response(self.get_context_data())
            
            response = self.delete(request, *args, **kwargs)
            logger.info('Book deleted successfully')
            return response
        except Exception as e:
            logger.error('Error deleting Book: %s %s', self.object.id, str(e))
            return redirect('gest-books')

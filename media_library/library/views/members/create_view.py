# from django.shortcuts import render, redirect
# from django.contrib.auth.decorators import login_required
#from django.utils.text import slugify

from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView
from library.models import Member
from library.forms import MemberForm
import logging

logger = logging.getLogger('library')

#-------------------------------------------------------------------------------------------------------
# [CBV] - CLASS BASED VIEW 
#-------------------------------------------------------------------------------------------------------

class CreateMemberView(LoginRequiredMixin, CreateView):

    model = Member
    form_class = MemberForm
    template_name = 'library/members/member_form.html'
    success_url = reverse_lazy('gest-members')


    def form_valid(self, form):
        """
        Overrides the form_valid method of CreateView to log the creation of a
        new Member and the details of the new member.

        Args:
            form (MemberForm): The form containing the submitted data.

        Returns:
            HttpResponseRedirect: A redirect to the success URL.

        Logs an info message with the user and member details.
        """
        try:
            logger.info('Create member - USER: %s', self.request.user)
            logger.debug('Member details: %s', form.cleaned_data)
            return super().form_valid(form)
        except Exception as e:
            logger.exception('Error occurred while creating member: %s', str(e))
            return super().form_invalid(form)



#-------------------------------------------------------------------------------------------------------
# [FBV] - FUNCTIONS BASED VIEWS
#-------------------------------------------------------------------------------------------------------

# @login_required
# def CreateBookView(request):
#     '''
#     Create a new Book instance.

#     GET:
#     Returns a form to create a new Book instance.

#     POST:
#     Creates a new Book instance with the given data and returns a redirect to
#     the list of books.
#     '''
#     form = BookForm()

#     if request.method == 'POST':
#         form = BookForm(request.POST)
#         if form.is_valid():
#             book = form.save(commit=False)
#             book.slug = slugify(book.title)
#             book.save()
#             return redirect('gest-books')

#     context = {
#         'form': form,
#     }
#     return render(request, 'library/books/book_form.html', context)
# from django.shortcuts import render, redirect
# from django.contrib.auth.decorators import login_required

from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import UpdateView
from library.models import Book
from library.forms import BookForm


''' UPDATE VIEW '''

''' [CBV] - CLASS BASED VIEW '''
class BookUpdateView(LoginRequiredMixin, UpdateView):
    model = Book
    form_class = BookForm
    template_name = 'library/books/book_form.html'
    slug_field = 'slug'  # Especifica que o lookup será feito pelo campo slug
    slug_url_kwarg = 'slug'
    success_url = reverse_lazy('gest-books')  # Redireciona após a atualização

    def form_valid(self, form):
        # Aqui você pode adicionar lógica adicional, se necessário
        return super().form_valid(form)


''' [FBV] - FUNCTION BASED VIEW '''
# @login_required
# def BookUpdateView(request, slug):
#     book = Book.objects.get(slug=slug)

#     form = BookForm(instance=book)

#     if request.method == 'POST':
#         form = BookForm(request.POST, instance=book)
#         if form.is_valid():
#             form.save()
#             return redirect('gest-books') 

#     context = {
#         'form': form
#     }
#     return render(request, 'library/books/book_form.html', context)
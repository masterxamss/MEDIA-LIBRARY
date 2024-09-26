# from django.shortcuts import render, redirect
# from django.contrib.auth.decorators import login_required

from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import UpdateView
from library.models import BoardGame
from library.forms import BoardGameForm


''' UPDATE VIEW '''

''' [CBV] - CLASS BASED VIEW '''
class BoardGameUpdateView(LoginRequiredMixin, UpdateView):
    model = BoardGame
    form_class = BoardGameForm
    template_name = 'library/board_games/board_game_form.html'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    success_url = reverse_lazy('gest-games')

    def form_valid(self, form):
        return super().form_valid(form)


''' [FBV] - FUNCTION BASED VIEW '''
# @login_required
# def BoardGameUpdateView(request, slug):
#     board_game = BoardGame.objects.get(slug=slug)

#     form = BoardGameForm(instance=book)

#     if request.method == 'POST':
#         form = BoardGameForm(request.POST, instance=book)
#         if form.is_valid():
#             form.save()
#             return redirect('gest-games') 

#     context = {
#         'form': form
#     }
#     return render(request, 'library/board_games/board_game_form.html', context)
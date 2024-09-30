# from django.shortcuts import render, get_object_or_404
# from django.contrib.auth.decorators import login_required

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView
from library.models import BoardGame


class BoardGamesView(LoginRequiredMixin,ListView):
    template_name = "library/board_games/gest_board_games.html"
    model = BoardGame
    ordering = ["name"]
    context_object_name = "board_games"
    paginate_by = 10

    error = None

    def get_queryset(self):
        queryset = super().get_queryset()
        
        # Get POST parameters if any
        search_name = self.request.POST.get('search_name','').strip()

        # Apply filters based on POST data
        if search_name:
            queryset = queryset.filter(name__icontains=search_name)
            if queryset.count() == 0:
                self.error = "Aucun Jeux ne correspond à votre recherche."

        return queryset

    def get_context_data(self, **kwargs):    
        context = super().get_context_data(**kwargs)
        
        games = BoardGame.objects.all()
        context["total"] = games.count()
        context["error"] = self.error
        context["return_all"] = 'checked' if self.request.POST.get('return_all') else ''

        return context

    def post(self, request, *args, **kwargs):
        """
        Handles a POST request to filter books.

        Reuses the get method for filtering logic.
        """
        return self.get(request, *args, **kwargs)

class BoardGameDetailView(LoginRequiredMixin, DetailView):
    model = BoardGame
    template_name = "library/gest_media.html"
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    context_object_name = 'game_detail'

# @login_required
# def LibraryBoardGamesDetailView(request, slug):
#     identified_media = get_object_or_404(BoardGame, slug=slug)
#     return render(request, "library/gest_media.html", {
#         "game_detail": identified_media
#     })


from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView
from library.models import BoardGame


class BoardGamesView(ListView):
    template_name = "library/board_games/gest_board_games.html"
    model = BoardGame
    ordering = ["name"]
    context_object_name = "board_games"
    paginate_by = 10

    error = None

    def get_queryset(self):
        """
        Override the default queryset to apply filtering based on the POST request.

        Retrieves the BoardGames from the database and applies the filters based on
        the POST request. If the search_name field is not empty, filters the
        BoardGames by the search_name field. If the search returns no results, sets
        the error attribute of the view instance to the appropriate error message.

        Returns:
            QuerySet: The filtered queryset of BoardGames.
        """
        queryset = super().get_queryset()

        search_name = self.request.POST.get('search_name', '').strip()

        if search_name:
            queryset = queryset.filter(name__icontains=search_name)
            if queryset.count() == 0:
                self.error = "Aucun Jeux ne correspond à votre recherche."

        return queryset

    def get_context_data(self, **kwargs):
        """
        Adds additional context to the response.

        Adds the error message if any, total board games, and the status of the filters and sorting options.

        Returns:
            dict: The context as a dictionary.
        """
        context = super().get_context_data(**kwargs)

        games = BoardGame.objects.all()
        context["total"] = games.count()
        context["error"] = self.error
        context["return_all"] = 'checked' if self.request.POST.get(
            'return_all') else ''
        context["user"] = self.request.user

        return context

    def post(self, request, *args, **kwargs):
        """
        Handles a POST request to filter books.

        Reuses the get method for filtering logic.
        """
        return self.get(request, *args, **kwargs)


class BoardGameDetailView(DetailView):
    model = BoardGame
    template_name = "library/gest_media.html"
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    context_object_name = 'game_detail'

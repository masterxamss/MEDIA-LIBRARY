from django.shortcuts import render
from django.core.paginator import Paginator
from django.views.generic import ListView
from itertools import chain
from django.db.models import Q
from library.models import Book, Cd, Dvd, BoardGame

class MediaListView(ListView):
    template_name = 'member/index.html'
    context_object_name = 'media_list'
    paginate_by = 10
    
    def get_queryset(self):
        """
        Return a list of all media items filtered by search query and media type.
        
        The method first fetches all media items from the database and then
        filters the results according to the search query and media type
        specified in the request's GET parameters.
        
        If no filters are applied, the method returns all media items.
        """
        books = Book.objects.all()
        cds = Cd.objects.all()
        dvds = Dvd.objects.all()
        boardgames = BoardGame.objects.all()

        search_query = self.request.GET.get('search', '').strip()
        books_query = self.request.GET.get('return_books')
        cds_query = self.request.GET.get('return_cds')
        dvds_query = self.request.GET.get('return_dvds')
        boardGames_query = self.request.GET.get('return_games')

        if search_query:
            books = Book.objects.filter(Q(title__icontains=search_query))
            cds = Cd.objects.filter(Q(title__icontains=search_query))
            dvds = Dvd.objects.filter(Q(title__icontains=search_query))
            boardgames = BoardGame.objects.filter(Q(name__icontains=search_query))

        media_queryset = []

        if books_query:
            media_queryset.extend(books)
        if cds_query:
            media_queryset.extend(cds)  
        if dvds_query:
            media_queryset.extend(dvds) 
        if boardGames_query:
            media_queryset.extend(boardgames)

        if not media_queryset:
            media_queryset = list(chain(books, cds, dvds, boardgames))
        
        for item in media_queryset:
            item.media_type = item.__class__.__name__

        return media_queryset


    def get_context_data(self, **kwargs):
        # Adiciona o combined_queryset ao contexto
        
        """
        Adiciona o combined_queryset ao contexto.
        
        Pagina o queryset combinado com self.paginate_by itens por página.
        Adiciona ao contexto o queryset paginado, o total de cada tipo de mídia e 
        os status dos filtros e opções de ordenação.
        """
        
        context = super().get_context_data(**kwargs)
        combined_queryset = self.get_queryset()
        
        # Pagina o queryset combinado
        paginator = Paginator(combined_queryset, self.paginate_by)  # Aplica paginação
        page = self.request.GET.get('page')

        # Obtenha a página atual de itens paginados
        media_list = paginator.get_page(page)

        total_books = Book.objects.count()
        total_cds = Cd.objects.count()
        total_dvds = Dvd.objects.count()
        total_games = BoardGame.objects.count()

        total_medias = total_books + total_cds + total_dvds + total_games
        
        # Adiciona ao contexto
        context['media_list'] = media_list
        context['total_medias'] = total_medias
        context['total_books'] = total_books
        context['total_cds'] = total_cds
        context['total_dvds'] = total_dvds
        context['total_games'] = total_games
        context['return_all'] = 'checked' if self.request.GET.get('return_all') else ''
        context['return_books'] = 'checked' if self.request.GET.get('return_books') else ''
        context['return_cds'] = 'checked' if self.request.GET.get('return_cds') else ''
        context['return_dvds'] = 'checked' if self.request.GET.get('return_dvds') else ''
        context['return_games'] = 'checked' if self.request.GET.get('return_games') else ''

        return context
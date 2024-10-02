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

    total_medias = 0

    def get_queryset(self):

        books = Book.objects.all()
        cds = Cd.objects.all()
        dvds = Dvd.objects.all()
        boardgames = BoardGame.objects.all()

        combined_queryset = list(chain(books, cds, dvds, boardgames))

        self.total_medias = len(combined_queryset)
        
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
            combined_queryset = list(chain(books, cds, dvds, boardgames))
        if books_query:
            books = Book.objects.all()
            combined_queryset = books
        if cds_query:
            cds = Cd.objects.all()
            combined_queryset = cds
        if dvds_query:
            dvds = Dvd.objects.all()
            combined_queryset = dvds
        if boardGames_query:
            boardgames = BoardGame.objects.all()
            combined_queryset = boardgames
        
        for item in combined_queryset:
            item.media_type = item.__class__.__name__

        return combined_queryset


    def get_context_data(self, **kwargs):
        # Adiciona o combined_queryset ao contexto
        context = super().get_context_data(**kwargs)
        combined_queryset = self.get_queryset()
        
        # Pagina o queryset combinado
        paginator = Paginator(combined_queryset, self.paginate_by)  # Aplica paginação
        page = self.request.GET.get('page')

        # Obtenha a página atual de itens paginados
        media_list = paginator.get_page(page)
        
        # Adiciona ao contexto
        context['media_list'] = media_list  # Adiciona ao contexto
        context['total_medias'] = self.total_medias
        context['total_books'] = Book.objects.count()
        context['total_cds'] = Cd.objects.count()
        context['total_dvds'] = Dvd.objects.count()
        context['total_games'] = BoardGame.objects.count()
        context['return_all'] = 'checked' if self.request.GET.get('return_all') else ''
        context['return_books'] = 'checked' if self.request.GET.get('return_books') else ''
        context['return_cds'] = 'checked' if self.request.GET.get('return_cds') else ''
        context['return_dvds'] = 'checked' if self.request.GET.get('return_dvds') else ''
        context['return_games'] = 'checked' if self.request.GET.get('return_games') else ''


        return context
# def home_member_view(request):
#     return render(request, 'member/index.html')
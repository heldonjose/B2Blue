from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView
import tmdbsimple as tmdb
import requests

from core.internal_models import Serie

tmdb.API_KEY = '9ae41b4b4c54fb22f0ac9124718c0ae5'
tmdb.REQUESTS_SESSION = requests.Session()


class MovieTemplateView(TemplateView):
    template_name = "core/movie/home.html"

    def get_context_data(self, **kwargs):
        list_series = []
        discover = tmdb.Discover()

        page = self.request.GET.get('page')
        if page:
            search = discover.tv(language='pt-BR', page=int(page))
        else:
            search = discover.tv(language='pt-BR', page=1)
        print('search', len(search['results']))
        for serie in search['results']:
            print(serie)
            list_series.append(Serie(serie))
        context = super().get_context_data(**kwargs)
        context['series'] = list_series
        context['page'] = 1 if not page else int(page)
        if not page or  int(page) == 1:
            context['list_page'] = [1, 2, 3]
        else:
            context['list_page'] = [ int(page)-1,  int(page),  int(page)+1]
        if int(page) in [10, 9, 8]:
            context['list_page'] = [8, 9, 10]

        return context

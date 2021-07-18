from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView


class MovieTemplateView(TemplateView):
    template_name = "core/movie/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context



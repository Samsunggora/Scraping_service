from django.shortcuts import render
from .models import Vacancy


def home_view(request):
    city = request.GET.get('city')
    language = request.GET.get('language')
    if city or language:
        _filter = {}
        if city:
            _filter['city__slug'] = city
        if language:
            _filter['language__slug'] = language
    qs = Vacancy.objects.filter(**_filter)
    return render(request, 'scraping/home_views.html', {"object_list": qs}, )

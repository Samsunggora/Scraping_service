from django.shortcuts import render
from .forms import FindForm
from .models import Vacancy


def home_view(request):
    form = FindForm()
    city = request.GET.get('city')
    language = request.GET.get('language')
    if city or language:
        _filter = {}
        if city:
            _filter['city__slug'] = city
        if language:
            _filter['language__slug'] = language
    else:
        return render(request, 'scraping/home_views.html')
    qs = Vacancy.objects.filter(**_filter)
    return render(request, 'scraping/home_views.html', {"object_list": qs,
                                                        'form': form,
                                                        })

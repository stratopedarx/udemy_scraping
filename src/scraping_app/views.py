from django.shortcuts import render

from .models import Vacation
from .forms import FindForm


def home_view(request):
    form = FindForm()
    city = request.GET.get('city')
    language = request.GET.get('language')
    qs = []
    if city or language:
        _filter = {}
        if city:
            _filter['city__slug'] = city
        if language:
            _filter['language__slug'] = language
        qs = Vacation.objects.filter(**_filter)
    return render(request=request, template_name='scraping_app/home.html', context={'object_list': qs, 'form': form})


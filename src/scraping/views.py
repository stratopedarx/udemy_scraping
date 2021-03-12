from django.shortcuts import render

import datetime


def home(request):
    date = datetime.datetime.now()
    name = 'Dave'
    context = {'date': date, 'name': name}
    return render(request=request, template_name='home.html', context=context)

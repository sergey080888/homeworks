import csv


from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.paginator import Paginator




def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    # получите текущую страницу и передайте ее в контекст
    # также передайте в контекст список станций на странице
    CONTEXT = []

    with open('data-398-2018-08-30.csv', encoding='UTF-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            CONTEXT.append({'Name':row['Name'], 'Street':row['Street'], 'District':row['District']})

    print(len(CONTEXT))
    page_number = int(request.GET.get("page", 1))
    paginator = Paginator(CONTEXT, 10)
    page = paginator.get_page(page_number)
    context = {
        'bus_stations': page,
        'page': page,
    }
    return render(request, 'stations/index.html', context)

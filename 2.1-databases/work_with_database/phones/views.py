from django.shortcuts import render, redirect
from phones.management.commands.import_phones import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    filter_dict = {'name': 'name', 'min_price': 'price', 'max_price': '-price', 'id': 'id'}
    filter_value = request.GET.get('sort', 'id')
    phones = Phone.objects.all().order_by(filter_dict[filter_value])
    context = {'phones': phones}
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phones = Phone.objects.all()
    for phone in phones:
        if phone.slug == slug:
            context = {'phone': phone}
            return render(request, template, context)

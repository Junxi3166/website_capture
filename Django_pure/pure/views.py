from django.shortcuts import render
from pure.models import ArtiInfo
from django.core.paginator import Paginator


def pure_index(request):
    return render(request,'pure_index.html')


def index(request):
    limit = 10
    arti_info = ArtiInfo.objects
    # arti_info = ArtiInfo.objects[:100]
    paginator = Paginator(arti_info, limit)
    page = request.GET.get('page', 1)
    print(request)
    print(request.GET)
    loaded = paginator.page(page)

    context = {
        'ArtiInfo': loaded
    }
    return render(request, 'index.html', context)

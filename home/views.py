from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.shortcuts import render

from wagtail.core.models import Page
from wagtail.search.models import Query
from . import models


def get_home(request):
    page = models.HomePage.objects.live()[0]
    context = page.get_context(request)
    return render(request, './home/home_page.html', context)

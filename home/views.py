from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.shortcuts import render

from wagtail.core.models import Page
from wagtail.search.models import Query
from . import models
from pa import models as pa_models
from lab import models as lab_models


def get_home(request):
    page = models.HomePage.objects.live()[0]
    context = page.get_context(request)
    context['pa_pages'] = pa_models.ProgramAssignment.objects.live()
    context['lab_pages'] = lab_models.Lab.objects.live()
    return render(request, './home/home_page.html', context)

from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.shortcuts import render

from wagtail.core.models import Page
from wagtail.search.models import Query
from . import models
from pa import models as pa_models
from lab import models as lab_models


def get_pa_index(request):
    page = models.PaIndexPage.objects.live()[0]
    context = page.get_context(request)
    context['pa_pages'] = pa_models.ProgramAssignment.objects.live()
    context['lab_pages'] = lab_models.Lab.objects.live()

    return render(request, './pa/pa_index_page.html', context)

def get_pa(request):

    pa_pages = pa_models.ProgramAssignment.objects.live()
    for page in pa_pages:

        if request.path_info == page.url:
            correct_page = page

    context = correct_page.get_context(request)
    context['pa_pages'] = pa_pages
    context['lab_pages'] = lab_models.Lab.objects.live()

    return render(request, './pa/program_assignment.html', context)

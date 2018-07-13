from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.shortcuts import render

from wagtail.core.models import Page
from wagtail.search.models import Query
from . import models
from pa import models as pa_models
from lab import models as lab_models


def get_lab_index(request):
    page = models.LabIndexPage.objects.live()[0]
    context = page.get_context(request)
    context['pa_pages'] = pa_models.ProgramAssignment.objects.live()
    context['lab_pages'] = lab_models.Lab.objects.live()

    return render(request, './lab/lab_index_page.html', context)

def get_lab(request):

    lab_pages = lab_models.Lab.objects.live()
    for page in lab_pages:
        if request.path_info == page.url:
            correct_page = page

    context = correct_page.get_context(request)
    context['lab_pages'] = lab_pages
    context['pa_pages'] = pa_models.ProgramAssignment.objects.live()

    return render(request, './lab/lab.html', context)

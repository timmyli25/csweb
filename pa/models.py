from django.db import models

# Create your models here.
from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel


class ProgramAssignment(Page):
    course = RichTextField(blank=True)
    patitle = RichTextField(blank=True)
    body = RichTextField(blank=True)


    content_panels = Page.content_panels + [
        FieldPanel('course', classname="full"),
        FieldPanel('patitle', classname="full"),
        FieldPanel('body', classname="full"),
    ]

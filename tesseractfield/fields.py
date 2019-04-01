from django import forms
from django.db import models


class TesseractWidget(forms.Textarea):
    template_name = 'tesseractfield/tesseract.html'

    class Media:
        js = ['tesseractfield/js/tesseract.js']


class TesseractField(models.TextField):

    def formfield(self, **kwargs):
        kwargs['widget'] = TesseractWidget
        return super(TesseractField, self).formfield(**kwargs)

from django.db import models

from tesseractfield.fields import TesseractField


class Article(models.Model):
    title = models.CharField(verbose_name='Title', max_length=50)
    p_content = models.TextField(verbose_name='Primany Content')
    s_content = TesseractField(verbose_name='Second Content')

    class Meta:
        verbose_name = 'Article'
        verbose_name_plural = 'Articles'
        ordering = ['title']

    def __str__(self):
        return self.title

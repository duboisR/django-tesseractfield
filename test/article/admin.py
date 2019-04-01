from django.contrib import admin
from django.forms import ModelForm
from article.models import Article

from tesseractfield.fields import TesseractWidget


class ArticleForm(ModelForm):
    class Meta:
        model = Article
        fields = '__all__'
        widgets = {
            'p_content': TesseractWidget(),
        }


class ArticleAdmin(admin.ModelAdmin):
    form = ArticleForm


admin.site.register(Article, ArticleAdmin)

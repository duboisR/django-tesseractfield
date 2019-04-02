[![PyPI version](https://badge.fury.io/py/django-tesseractfield.svg)](https://badge.fury.io/py/django-tesseractfield)

# django-tesseractfield

This module fills the need of having a **tesseractfield** that's usable in both
django models and forms.

![django-tesseractfield](http://www.giphy.com/gifs/8hYe9XW88QuL062sMe)

Makes use of [tesseract](https://opensource.google.com/projects/tesseract).

## Installation
- Run ``pip install django-tesseractfield``
- Add ``tesseractfield`` to your ``INSTALLED_APPS``
- Collect static files with ``./manage.py collectstatic``

## Usage
To activate tesseract transcription on your Django site, add this line to your URLconf:

```python
path('', include('tesseractfield.urls')),
```

In your models, you can use it like this:

```python
from django.db import models
from tesseractfield.fields import TesseractField

class MyModel(model.Model):
    content = TesseractField()
```

In your foms, you can use it like this:

```python
from django import forms
from tesseractfield.fields import TesseractWidget

class MyForm(forms.Form):
    content = forms.Textarea()

    class Meta:
        widgets = {
            'content': TesseractWidget(),
        }
```

## Maintainers
- [@duboisR](https://github.com/duboisR)

## Articles
- [Django Tesseract OCR](https://medium.com/@duboisr/django-et-tesseract-188d389ad4ba)

from django.urls import path

import tesseractfield.views


urlpatterns = [
    path('api/tesseract/', tesseractfield.views.TesseractView.as_view()),
]

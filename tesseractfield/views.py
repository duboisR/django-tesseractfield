from django.http import JsonResponse
from django.views import View

import tesseractfield.tesseract


class TesseractView(View):
    def post(self, request, format=None):
        file_obj = request.FILES.get('file', None)
        if file_obj:
            transcript = tesseractfield.tesseract.transcript(file_obj)
            return JsonResponse({'transcript': transcript}, status=200)
        return JsonResponse({}, status=204)

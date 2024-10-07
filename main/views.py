from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
import pytesseract
from PIL import Image
from pathlib import Path

class Read_Image_View(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request):
        try:
            pytesseract.pytesseract.tesseract_cmd = str(Path(__file__).parent.parent) + '\\Tesseract-OCR\\tesseract.exe'

            image = self.request.data['image']
            text = pytesseract.image_to_string(Image.open(image))

            return Response({'result': text}, status=200)
        except Exception as e:
            return Response({'error': '\'image\' parameter required. Supported file formats: .jpg, .png'}, status=422)
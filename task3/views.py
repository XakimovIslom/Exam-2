import base64
import json

from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView

from task3.models import Product
from task3.renderers import AES_IV, AES_SECRET_KEY, CustomAesRenderer
from task3.serializers import ProductSerializer

# newly added below


class ProductListAPIView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductListEncryptedView(APIView):
    renderer_classes = [CustomAesRenderer]

    def get(self, request):
        products = Product.objects.all()
        if products:
            serializer = ProductSerializer(products, many=True)
            data = serializer.data
        data = {"status": "success", "code": status.HTTP_200_OK, "data": data}
        return Response(data, status=status.HTTP_200_OK)


class DecryptProductList(APIView):
    def post(self, request, *args, **kwargs):
        encrypted_data = request.data["ciphertext"]
        enc = base64.b64decode(encrypted_data)
        cipher = AES.new(AES_SECRET_KEY, AES.MODE_CBC, AES_IV)
        try:
            decrypted_data = unpad(cipher.decrypt(enc), 16)
            decrypted_data = json.loads(decrypted_data)
            data = {"data": decrypted_data}
            return Response(data)
        except Exception as e:
            return Response({"data": f"An error- {e}"})

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import json


class GeneratePostCaptions(APIView):
    def post(req):
        return Response(
            {"data": ["hii"], "message": "hello from GeneratePostCaptions"},
            status.HTTP_200_OK,
        )

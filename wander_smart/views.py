from rest_framework.views import APIView
from rest_framework.response import Response


class GenerateTripPlan(APIView):
    def get(self, request):
        names = ["sagar", "kalpu", "ruby", "chinki"]
        return Response(names)

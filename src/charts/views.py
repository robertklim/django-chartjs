import requests

from django.shortcuts import render
from django.views.generic import View

from rest_framework.views import APIView
from rest_framework.response import Response

class HomeView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'charts.html', {})

class ChartData(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        owner = 'django'
        repo = 'django'
        url = f'https://api.github.com/repos/{owner}/{repo}/stats/participation'

        res = requests.get(url).json()

        return Response(res)
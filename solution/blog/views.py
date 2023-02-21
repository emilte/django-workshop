from django.views import View
from django.http import JsonResponse


class TestView(View):

    def get(self, request):
        data = {'test': 123}
        return JsonResponse(data=data)

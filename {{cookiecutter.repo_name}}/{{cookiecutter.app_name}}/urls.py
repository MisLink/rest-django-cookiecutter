from django.http import JsonResponse
from django.urls import include
from django.urls import path

from .users.tasks import func
from .users.urls import router


def ping(request):
    func.delay()
    return JsonResponse("pong!", safe=False)


urlpatterns = [
    path("ping/", ping, name="ping"),
    path("api/1.0/", include([path("", include(router.urls))])),
]

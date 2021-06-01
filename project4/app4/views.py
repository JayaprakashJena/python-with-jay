from django.http import HttpResponse


def showInfo(http_request):
    message="hello word"
    return HttpResponse(message)

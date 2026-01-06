from django.http import HttpRequest, HttpResponse


def login(request: HttpRequest) -> HttpResponse:
    return HttpResponse('login page')
    
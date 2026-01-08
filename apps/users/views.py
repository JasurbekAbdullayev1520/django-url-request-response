from django.http import HttpRequest, HttpResponse


def home_view(request: HttpRequest) -> HttpResponse:
    return HttpResponse()

def get_user_by_id_view(request: HttpRequest, id: int) -> HttpResponse:
    return HttpResponse(f'salom, {id}')

def get_post_by_title_view(request: HttpRequest, title: str) -> HttpResponse:
    return HttpResponse(f'salom, {title}')

def get_product_by_uuid_view(request: HttpRequest, id: str) -> HttpResponse:
    return HttpResponse(f'salom, {id}')

def get_sub_news_by_path_view(request: HttpRequest, path: str) -> HttpResponse:
    return HttpResponse(f'salom, {path}')

def calculators_view(request):
    a = request.GET.get('a')
    b = request.GET.get('b')

    if not a or not b:
        return HttpResponse("a va b kerak")

    return HttpResponse(int(a) + int(b))

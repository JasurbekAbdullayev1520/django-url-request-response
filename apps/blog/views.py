
from django.http import HttpResponse

def get_blogs_by_uuid_view(request, uuid):
    return HttpResponse(f"Blog uuid: {uuid}")


# Create your views here.

from django.http import HttpResponse


def test(request):
    if request.user.is_superuser:
        1/0
    else:
        return HttpResponse("Not authorized, only superuser")

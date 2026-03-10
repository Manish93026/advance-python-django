from django.http import HttpResponse


def test_sos1(request):
    return HttpResponse("<h1>Hello Django in sos1</h1>")
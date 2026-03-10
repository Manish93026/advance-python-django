from django.http import HttpResponse


def test_ors(request):
    return HttpResponse("<h1>Hello Django not sos</h1>")

from django.http import HttpResponse


def test_ORS1(request):
    return HttpResponse("<h1>Hello Django ORS1</h1>")

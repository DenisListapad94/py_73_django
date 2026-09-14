from django.shortcuts import render, HttpResponse

def test_view(request):
    return HttpResponse("<h1>test view</h1>")


def test_view1(request, username):
    return HttpResponse(f"<h1>Hi: {username}</h1>")
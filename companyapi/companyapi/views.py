from django.http import HttpResponse

def home_url(request):
    print("On home page: ")
    return HttpResponse("<h1> Welcome to HomePage <h1> <marquee> krishna is great </marquee>")
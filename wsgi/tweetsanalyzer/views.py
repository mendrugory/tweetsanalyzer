__author__ = 'mendrugory'

from django.http import HttpResponse

def index(request):
    html = "<html><body>WELCOME</body></html>"
    return HttpResponse(html)

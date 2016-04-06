from os.path import basename, getsize, join
from wsgiref.util import FileWrapper

from django.shortcuts import render
from django.http import HttpResponse

from Cisplatin.settings import BASE_DIR
from Cisplatin_App.utils.utils import http_headers

# Render the homepage, with PGP key
def home(request):
    # Load up the PGP key
    with open(join(BASE_DIR, "static/pgp/public-key.asc"), "r") as public:
        key = public.read()
    return http_headers(render(request, 'home.html', {'PGP_KEY' : key}))

# Return Simon's resume
def resume(request):
    filename = join(BASE_DIR, "static/pdf/Simon Hajjar.pdf")
    wrapper = FileWrapper(file(filename))
    response = http_headers(HttpResponse(wrapper, content_type='application/pdf'))
    response['Content-Disposition'] = 'attachment; filename="%s"' % basename(filename)
    response['Content-Length'] = getsize(filename)
    return response

# Return the robots.txt
def robots(request):
    return http_headers(render(request, 'robots.txt'))

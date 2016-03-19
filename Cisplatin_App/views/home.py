from os.path import basename, getsize
from wsgiref.util import FileWrapper

from django.shortcuts import render
from django.http import HttpResponse

# Render the homepage, with PGP key
def home(request):
    # Load up the PGP key
    with open("static/pgp/public-key.asc", "r") as public:
        key = public.read()
    return render(request, 'home.html', {'PGP_KEY' : key})

# Return Simon's resume
def resume(request):
    filename = "static/pdf/Simon Hajjar.pdf"
    wrapper = FileWrapper(file(filename))
    response = HttpResponse(wrapper, content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="%s"' % basename(filename)
    response['Content-Length'] = getsize(filename)
    return response

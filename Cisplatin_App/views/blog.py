from django.shortcuts import render
from Cisplatin_App.utils.utils import http_headers

# Exploits Using .xlsx Files
def exploits_using_xlsx_files(request):
    return http_headers(render(request, 'blogs/blog-exploits_using_xlsx_files.html'))

# Render the blog page
def home(request):
    return exploits_using_xlsx_files(request)

from django.shortcuts import render
from Cisplatin_App.utils.utils import http_headers

# Render the blog page
def home(request):
    return http_headers(render(request, 'blogs/blog-home.html'))

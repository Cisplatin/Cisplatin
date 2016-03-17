from django.shortcuts import render

# Render the homepage
def home(request):
    return render(request, 'home.html')

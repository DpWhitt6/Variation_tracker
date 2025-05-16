from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the index view.")

def form_view(request):
    if request.method == 'POST':
        # Handle form submission
        pass
    else:
        # Render the form
        pass
    return render(request, 'form_template.html')
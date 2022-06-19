from django.shortcuts import render

# Create your views here.


def index(request):

    """The homepage for kisik"""

    return render(request, 'cat/index.html')
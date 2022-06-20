from django.shortcuts import render

from .models import Topic


def index(request):

    """The homepage for kisik"""

    return render(request, 'cat/index.html')


def topics(request):

    """Shows all topics"""

    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics}

    return render(request, 'cat/topics.html', context)

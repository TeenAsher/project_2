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


def topic(request, topic_id):

    """Shows a single topic and its entries"""

    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}

    return render(request, 'cat/topic.html', context)

from django.shortcuts import render, redirect

from .models import Topic
from .forms import TopicForm


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


def new_topic(request):

    """Adding a new topic"""

    if request.method != 'POST':
        # No data submitted; create a blank form
        form = TopicForm()
    else:
        # POST data submitted, process data
        form = TopicForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('cat:topics')

    # Display a blank or invalid form
    context = {'form': form}
    return render(request, 'cat/new_topic.html', context)

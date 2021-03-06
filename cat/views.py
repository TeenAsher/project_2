from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .models import Topic, Entry
from .forms import TopicForm, EntryForm


def index(request):

    """The homepage for kisik"""

    return render(request, 'cat/index.html')

@login_required
def topics(request):

    """Shows all topics"""

    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics}

    return render(request, 'cat/topics.html', context)

@login_required
def topic(request, topic_id):

    """Shows a single topic and its entries"""

    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}

    return render(request, 'cat/topic.html', context)

@login_required
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

@login_required
def new_entry(request, topic_id):

    """Adding a new entry for the particular topic"""

    topic = Topic.objects.get(id=topic_id)

    if request.method != 'POST':
        # No data submitted; create a blank form
        form = EntryForm()
    else:
        # POST data submitted; process data
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return redirect('cat:topic', topic_id=topic_id)

    # Display a blank or invalid form
    context = {'topic': topic, 'form': form}
    return render(request, 'cat/new_entry.html', context)

@login_required
def edit_entry(request, entry_id):

    """Editing the entry from the list"""

    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic

    if request.method != 'POST':
        # Initial request; pre-fill form with the current entry
        form = EntryForm(instance=entry)
    else:
        # POST data submitted; process data
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('cat:topic', topic_id=topic.id)

    context = {'entry': entry, 'topic': topic, 'form': form}
    return render(request, 'cat/edit_entry.html', context)

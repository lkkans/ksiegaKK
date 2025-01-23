from django.shortcuts import render, redirect
from .models import Topic, Comment
from .forms import CommentForm

def topic_list(request):
    topics = Topic.objects.all()
    return render(request, 'complaints/topic_list.html', {'topics': topics})

def topic_detail(request, pk):
    topic = Topic.objects.get(pk=pk)
    comments = topic.comments.all()

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.topic = topic
            new_comment.save()
            return redirect('topic_detail', pk=pk)
    else:
        form = CommentForm()

    return render(request, 'complaints/topic_detail.html', {
        'topic': topic,
        'comments': comments,
        'form': form
    })

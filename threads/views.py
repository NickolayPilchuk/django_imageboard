from django.shortcuts import render,redirect,HttpResponse
from .models import Threads,Comments
from .forms import Thread_form,Comment_form
def main(request):
    threads = Threads.objects.all()
    context = {'threads':threads}
    return render(request,'threads\main_page.html',context)

def thread(request,thread_id):
    thread = Threads.objects.get(id=thread_id)
    if request.method == 'POST':
        form = Comment_form(request.POST,request.FILES)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.META.get('REMOTE_ADDR')
            comment.thread = thread
            comment.save()
            return redirect('/threads/'+ str(thread_id))
    else:
        comments = Comments.objects.filter(thread=thread)
        form = Comment_form
        context = {'thread': thread, 'comments': comments, 'form': form}
    return render(request, 'threads\\thread_page.html', context)


def new_thread(request):
    if request.method == 'POST':
        form = Thread_form(request.POST, request.FILES)
        if form.is_valid():
            thread = form.save(commit=False)
            thread.user = request.META.get('REMOTE_ADDR')
            thread.save()
            return redirect(main)
    else:
        form = Thread_form
        context = {'form':form}
    return render(request,'threads\\thread_form.html',context)
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect

from fb.models import UserPost
from fb.models import UserComment
from fb.forms import UserPostForm
from fb.forms import UserCommentForm

def index(request):
    if request.method == 'GET':
        posts = UserPost.objects.all().order_by('-date_added')
        # links = {}
        baseurl = "http://localhost:8000"

        for index in range(len(posts)):
            posts[index].text = posts[index].text[:15]
            posts[index].link = baseurl + "/post/" + str(posts[index].id)

        form = UserPostForm()
    
        context = {
            'posts': posts,
            'form': form
        }
        return render(request, 'index.html', context)

    elif request.method == 'POST':
    	form = UserPostForm(request.POST)
    	if form.is_valid():
    		text = form.cleaned_data['text']
    		post = UserPost(text=text)
    		post.save()
    	return redirect('index')

def custom_redirect(url_name, *args, **kwargs):
    from django.core.urlresolvers import reverse 
    import urllib
    url = reverse(url_name, args = args)
    params = urllib.urlencode(kwargs)
    return HttpResponseRedirect(url + "?%s" % params)

def post_page(request, post_id):
    if request.method == 'GET':
        post_content = UserPost.objects.filter(pk=post_id)[0]
        comment_form = UserCommentForm()
        comments = UserComment.objects.filter(post_id=post_id).order_by('-date_added')

        context = {
            'post_id': post_id,
            'post_content': post_content,
            'comment_form': comment_form,
            'comments': comments
        }
        return render(request, 'post_page.html', context)

    if request.method == 'POST':
        form = UserCommentForm(request.POST)
        post_id = request.POST.get('post_id')

        if form.is_valid():
            text = form.cleaned_data['text']
            comment = UserComment(text=text, post_id=post_id)
            comment.save()

        return custom_redirect('post', post_id)

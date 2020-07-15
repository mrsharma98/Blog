from django.shortcuts import render,get_object_or_404,redirect
from django.utils import timezone
from blog.models import Post,Comment
from django.urls import reverse_lazy

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from django.views.generic import (TemplateView, ListView,
                                  DetailView, CreateView,
                                  UpdateView, DeleteView)

from blog.forms import PostForm,CommentForm

## importing for method views.


# Create your views here.

class AboutView(TemplateView):
    template_name = 'about.html'
    # this tells us that it belongs to about.html
    # and its view attached in url to some url will send us to that page.


class PostListView(ListView):
    model = Post
    # above line connects this CVB to the Post model

    def get_queryset(self):
    # this method allows us to use Django's ORM
    # by using get_query_set we are basically almost doing a query.
    # this is like a sql query on the model.
        return Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
        # Post -> grab the Post model
        # object -> all the object there
        # filter() -> filter out on the given condition
        # grabbing the published_date and
        # __lte means less than or equal to
        # timezone.now() is the current time
        # and then order them by the published_date
        # order_by() -> will order them.
        # -pubished_date -> that dash before the published_date represents decending order.


class PostDetailView(DetailView):
    model = Post

# the Mixins are just like decorators
# but mixins are used by CBV.
# these are basically classes.
# LoginRequiredMixin basically assures that
#the user performing some task is currently logged in
class CreatePostView(LoginRequiredMixin, CreateView):
    # setting up the login and it will go tp login
    login_url = '/login/'
    redirect_field_name = 'blog/post_detail.html'
    # the above 2 fields are the attributes of LoginRequiredMixin.

    # we need to import PostForm as we want to create a post
    form_class = PostForm

    model = Post


class PostUpdateView(LoginRequiredMixin, UpdateView):
    # setting up the login and it will go tp login
    login_url = '/login/'
    redirect_field_name = 'blog/post_detail.html'
    # the above 2 fields are the attributes of LoginRequiredMixin.
    form_class = PostForm

    model = Post


class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    success_url = reverse_lazy('blog/post_list')
    # if we delete a post then it will be redirected to post_list page


class DraftListView(LoginRequiredMixin, ListView):
    login_url = '/login/'
    redirect_field_name = 'blog/post_list.html'
    model = Post

    def get_queryset(self):
        return Post.objects.filter(published_date__isnull=True).order_by('created_date')
        # Grab the Post which donot have a published_date
        # and then order them by created_date



###########################################
###########################################

# function Based Views.

@login_required
def post_publish(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.publish()
    return redirect('post_detail', pk=pk)


@login_required
def add_comment_to_post(request, pk):
    # if someone tries to do comment on some post
    # we are taking request and pk that links the comment to the actual post.
    post = get_object_or_404(Post, pk=pk)
    # get_object_or_404() -> this says either get that object or 404 page.
    # post -> POST object
    if request.method == 'POST':
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            # comment.post will be equal to the post variable we have defined in the models.
            comment.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = CommentForm()
        # if that condition becomes false
        # then here in the else part
        # we are again providing the user the CommentForm to fill out again.
        # means rendering them to the comment_form
    return render(request, 'blog/comment_form.html', {'form':form})

@login_required
def comment_approve(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.approve()
    #we have called the approve method on the actual model object.
    return redirect('post_detail', pk=comment.post.pk)

@login_required
def comment_remove(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    post_pk = comment.post.pk
    # assigning the post's pk to a variable
    # comment_approved and this method is almost same.
    # but here we want the pk of that post even after deleting it
    # so as to redirect the page
    comment.delete()
    return redirect('post_detail', pk=post_pk)

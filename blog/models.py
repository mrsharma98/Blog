from django.db import models
from django.utils import timezone
from django.urls import reverse


# Create your models here.

# Post Section
class Post(models.Model):
    author = models.ForeignKey('auth.User')
    # conneting author to the authorized user or superuser on the website.
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now())
    published_date = models.DateTimeField(blank=True, null=True)

    # if the user published his/her post.
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    # to show the approved comments on the post
    def approve_comments(self):
        return self.comments.filter(approved_comments=True)
        # comments from the comment model

    def get_absolute_url(self):
        return reverse("post_detail", kwargs={'pk':self.pk})
        # after creation of the post and publishing it
        # the website should direct it to somewhere
        # so get_absolute_url does this work and
        # it will redirect it to "post_detail" and
        # takes the pk of that post
        #so that it lands up on the post detail for the same post.


    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey('blog.Post', related_name='comments')
    # this will connect each comment to te actual post.
    # each post will be connected to blog post
    author = models.CharField(max_length=200)
    text = models.TextField()
    create_date = models.DateTimeField(default=timezone.now())
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def get_absolute_url(self):
        return reverse("post_list")
        # after commenting on the post
        # it will redirect the user to the home page which is "post_list"

    def __str__(self):
        return self.text

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    post_title = models.CharField(max_length=200)
    post_content = models.TextField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    # category = models.ForeignKey(
    #     Category, on_delete=models.SET_NULL, null=True, blank=True
    # )
    # tag = models.ManyToManyField(Tag, blank=True)

    # view_count = models.PositiveBigIntegerField(default=0)

    # liked_users = models.ManyToManyField(
    #     User,
    #     related_name="liked_posts",
    #)

    def __str__(self):
        return self.post_title

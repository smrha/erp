from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User

class Post(models.Model):
    STATUS_CHOICES = (
        ('d', 'پیش نویس'),
        ('p', 'منتشر شده')
    )
    title = models.CharField(max_length=256)
    slug = models.SlugField(max_length=256, unique_for_date='publish')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='d')

    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:post_detail', 
                        args=[self.publish.year, 
                            self.publish.month, 
                            self.publish.day, 
                            self.slug])
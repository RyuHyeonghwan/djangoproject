from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.
class Post(models.Model):
    category_choices=(('일상글','일상글'),('공부글','공부글'))
    title = models.CharField(max_length = 30)
    category = models.CharField(max_length=30, choices=category_choices, default='일상글',verbose_name='카테고리종류')
    content = models.TextField()
    writer = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add = True)
    updatd_at = models.DateTimeField(auto_now = True)


class Comment(models.Model):
    post = models.ForeignKey('Post',on_delete=models.CASCADE)
    content = models.TextField()
    writer = models.ForeignKey(User,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.content
    

class HashTag(models.Model):
    post = models.ForeignKey('Post',on_delete=models.CASCADE)    
    writer = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=10)

    def __str__(self):
        return self.name
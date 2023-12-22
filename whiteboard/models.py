from django.db import models
from django.contrib.auth.models import AbstractUser


class MyUser(AbstractUser):
    avatar = models.ImageField()
    description = models.TextField()

    class Meta(AbstractUser.Meta):
        pass


# Create your models here.
class Post(models.Model):
    text = models.TextField(blank=False,null=False)
    pict = models.ImageField(blank=True)
    user = models.ForeignKey("MyUser", on_delete=models.SET_DEFAULT, default=0)




class Comment(models.Model):
    text = models.TextField(blank=False,null=False)
    pict = models.ImageField(blank=True)
    post = models.ForeignKey("Post", on_delete=models.CASCADE,)
    user = models.ForeignKey("MyUser", on_delete=models.SET_DEFAULT, default=0)
    parent = models.ForeignKey(
        'self',
        default=None,
        blank=True, null=True,
        on_delete=models.CASCADE,
        related_name='parent_comment',
        verbose_name='parent comment'
    )

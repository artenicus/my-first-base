from django.conf import settings
from django.db import models
from django.utils import timezone

class Post(models.Model):
    Autor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    Tytuł_Rozwiązania = models.CharField(max_length=200)
    Treść = models.TextField()
    Data_Utworzenia = models.DateTimeField(default=timezone.now)
    Data_Publikacji = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.Data_Publikacji = timezone.now()
        self.save()

    def __str__(self):
        return self.Tytuł_Rozwiązania

    def approved_comments(self):
        return self.comments.filter(approved_comment=True)

class Comment(models.Model):
    post = models.ForeignKey('blog.Post', on_delete=models.CASCADE, related_name='comments')
    Autor = models.CharField(max_length=200)
    Treść = models.TextField()
    Data_Utworzenia = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.Treść


# Create your models here.

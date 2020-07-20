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
# Create your models here.

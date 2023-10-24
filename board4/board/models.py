from django.db import models

# Create your models here.
class Article(models.Model):
    # SQL) VARCHAR
    title = models.CharField(max_length=200)
    #SQL) TEXT
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)# 생성될때만저장
    updated_at = models.DateTimeField(auto_now=True)# 생성되고 수정될때마다 저장
from django.db import models

# Create your models here.


class Category (models.Model):
    name=models.CharField(max_length=225)
    created=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class news(models.Model):
    title=models.CharField(max_length=200)
    category = models.ForeignKey(Category, related_name="category_news", on_delete = models.CASCADE, blank=True, null=True)
    description=models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
from django.contrib import admin
from . models import news,Category

# Register your models here.
admin.site.register(news)
admin.site.register(Category)
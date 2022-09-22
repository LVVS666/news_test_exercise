from django.db import models


class TypeNews(models.Model):
    name = models.CharField(max_length=50)
    color = models.CharField(max_length=50)

class News(models.Model):
    title = models.CharField(max_length=50)
    discriptions = models.CharField(max_length=100)
    full_discriptions = models.TextField()
    type_news = models.ForeignKey(TypeNews,blank=True,
        null=True,on_delete=models.SET_NULL)






from django.forms import ModelForm
from .models import News,TypeNews

class NewsForm(ModelForm):
    
    class Meta:
        model = News
        fields = ("title","discriptions","full_discriptions","type_news")



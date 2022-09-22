from django.shortcuts import render
from .models import News,TypeNews
from django.core.paginator import Paginator

def news_post(request):
    template = "news_post/news_post.html"
    news = News.objects.all()
    paginator = Paginator(news, 5)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    context = {
        "page_obj":page_obj
    }
    return render(request, template,context)


    
from django.shortcuts import render
from app01 import models
# Create your views here.

def articles(request,*args,**kwargs):

    # from django.urls import reverse
    # print(reverse('art', kwargs=kwargs))
    # print(request.path_info)
    conf = {}
    for k,v in kwargs.items():
        kwargs[k] = int(v)
        if v == '0':
            pass
        else:
            conf[k] = v

    category = models.category

    # print(category)
    # for row in category:
    #     print(row[0])
    # return
    articleType = models.ArticleType.objects.all()

    result = models.Article.objects.filter(**conf)

    return render(request, 'article.html', {
        'res': result,
        'category' : category,
        'articleType': articleType,
        'arg_dict': kwargs
    })

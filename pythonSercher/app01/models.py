from django.db import models

# Create your models here.

# class Category(models.Model):
#     caption = models.CharField(max_length=16)

category = [
    (1, 'python之路'),
    (2, '从删库到跑路'),
    (3, '从入门到放弃'),
    (4, '皮皮虾我们走'),
    (5 , '程虎好好哦'),
]

class ArticleType(models.Model):
    caption = models.CharField(max_length=16)


class Article(models.Model):
    title = models.CharField(max_length=32)
    content = models.CharField(max_length=255)

    # category = models.ForeignKey(Category, on_delete=models.CASCADE)
    article_type = models.ForeignKey(ArticleType, on_delete=models.CASCADE)

    category_id = models.IntegerField(category)

from django import template
from django.utils.safestring import mark_safe

register = template.Library()

@register.simple_tag
def filter_all(tag, arg_dict):
    ref = '--'
    if tag == 'category':
        if arg_dict['category_id'] == 0:
            ref = '<a class="nowHref" href="article-0-%s.html">全部</a>' % arg_dict['article_type_id']
        else:
            ref = '<a href="article-0-%s.html">全部</a>' % arg_dict['article_type_id']

    if tag == 'article_type':
        if arg_dict['article_type_id'] == 0:
            ref = '<a class="nowHref" href="article-%s-0.html">全部</a>' % arg_dict['category_id']
        else:
            ref = '<a href="article-%s-0.html">全部</a>' % arg_dict['category_id']
    return mark_safe(ref)

@register.simple_tag
def filterOne(tag, arg_dict , data):
    ref = []
    if (tag == 'category'):
        for row in data:
            if row[0] == arg_dict['category_id']:
                temp = '<a class="nowHref" href="article-%s-%s.html">%s</a>' % (row[0], arg_dict['article_type_id'],row[1])
            else:
                temp = '<a href="article-%s-%s.html">%s</a>' % (row[0], arg_dict['article_type_id'],row[1])
            ref.append(temp)
    if tag == 'article_type':
        for row in data:
            if row.id == arg_dict['article_type_id']:
                temp = '<a class="nowHref" href="article-%s-%s.html">%s</a>' % (arg_dict['category_id'],row.id,row.caption)
            else:
                temp = '<a href="article-%s-%s.html">%s</a>' % (arg_dict['category_id'],row.id,row.caption)
            ref.append(temp)
    return mark_safe(''.join(ref))


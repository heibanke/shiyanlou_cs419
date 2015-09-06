#coding=utf-8

from jizhang.models import Category

def sort_categories(categories,list):
    for category in categories:
        list.append(category)
        sort_categories(category.childs.all(),list)
	
def get_sorted_categories(username):
    categories=[]
    category_list = Category.objects.filter(user__username=username).filter(p_category=None).all()
    sort_categories(category_list,categories)
    return categories


#coding=utf-8

from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.http import HttpResponseRedirect

#myApp package
from jizhang.models import Item, Category
# from jizhang.forms import ItemForm, CategoryForm, NewCategoryForm
# from jizhang.data_format_func import get_sorted_categories

        
# Create your views here.
@login_required
def categories(request, template_name='jizhang/categories.html'):
    if request.method == 'POST':
        ## delete categories
        pass
    
    # shiyan6
    category_list = Category.objects.filter(user__username=request.user.username).all()
    return render(request, template_name, {"categories":category_list})

@login_required
def show_category(request, pk, template_name='jizhang/items.html'):
    if request.method == 'POST':
        # delete items
        pass
    
    item_list = Item.objects.filter(category__user__username=request.user.username).filter(category__id=pk).order_by('price')
    return render(request, template_name, {'items':item_list})

@login_required    
def edit_category(request,pk):
    pass

@login_required
def new_category(request):
    pass


@login_required
def items(request, template_name='jizhang/items.html'):
    if request.method == 'POST':
        ## delete items
        pass
    item_list = Item.objects.filter(category__user__username=request.user.username).order_by('price')
    return render(request, template_name, {'items':item_list})


@login_required 
def edit_item(request, pk):
    pass


@login_required 
def new_item(request):
    pass


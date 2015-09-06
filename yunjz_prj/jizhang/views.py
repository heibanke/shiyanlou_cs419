#coding=utf-8

from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.http import HttpResponseRedirect

#myApp package
from jizhang.models import Item, Category
from jizhang.forms import ItemForm, CategoryForm, NewCategoryForm
from jizhang.data_format_func import get_sorted_categories

# shiyan7

        
# Create your views here.
@login_required
def categories(request, template_name='jizhang/categories.html'):
    if request.method == 'POST':
        ## delete categories
        pass
    
    # shiyan6
    #category_list = Category.objects.filter(user__username=request.user.username).all()

    # shiyan7
    return render(request, template_name, {"categories":get_sorted_categories(request.user.username)})

@login_required
def show_category(request, pk, template_name='jizhang/items.html'):
    if request.method == 'POST':
        # delete items
        pass
    
    item_list = Item.objects.filter(category__user__username=request.user.username).filter(category__id=pk).order_by('price')
    return render(request, template_name, {'items':item_list})

@login_required    
def edit_category(request,pk, template_name='jizhang/new_category.html'):
    out_errors = []
    if request.method == 'POST':
        form = CategoryForm(request,data=request.POST)
        if form.is_valid():
            form.save(pk)
            return HttpResponseRedirect("/jizhang/categories")
    else:
        category_list = get_object_or_404(Category, id=pk) 
        form = CategoryForm(request,instance=category_list)
    return render(request, template_name,{'form':form})

@login_required
def new_category(request, template_name='jizhang/new_category.html'):
    if request.method == 'POST':
        form = NewCategoryForm(request,data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/jizhang/categories")
    else:
        form = NewCategoryForm(request)
    return render(request, template_name, {'form':form})


@login_required
def items(request, template_name='jizhang/items.html'):
    if request.method == 'POST':
        ## delete items
        pass
    item_list = Item.objects.filter(category__user__username=request.user.username).order_by('price')
    return render(request, template_name, {'items':item_list})


@login_required 
def edit_item(request, pk, template_name='jizhang/new_item.html'):
    if request.method == 'POST':

        form = ItemForm(request,data=request.POST)
        if form.is_valid():
            form.save(pk)
            return HttpResponseRedirect("/jizhang")
    else:
        item_list = get_object_or_404(Item, id=pk)
        form = ItemForm(request,instance=item_list)

    return render(request, template_name,{'form':form})


@login_required 
def new_item(request, template_name='jizhang/new_item.html'):
    if request.method == 'POST':
        form = ItemForm(request,data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/jizhang")
    else:
        form = ItemForm(request,initial={'pub_date':timezone.now().date()})

    return render(request, template_name,{'form':form})


#coding=utf-8

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils import timezone

#myApp package
from jizhang.models import Item, Category
from jizhang.forms import ItemForm, CategoryForm, NewCategoryForm

# Create your views here.
@login_required
def categorys(request, template_name='jizhang/categorys.html'):
    if request.method == 'POST':
        ## delete categorys
        pass

    category_list = Category.objects.filter(user__username=request.user.username).all()
    return render(request, template_name, {"categorys":category_list})

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
            form.save()
            return HttpResponseRedirect("/jizhang/categorys")
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
            return HttpResponseRedirect("/jizhang/categorys")
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
            new_item = form.save()
            new_item.id=pk
            form.save()
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
            new_item = form.save()
            new_item.save()
            return HttpResponseRedirect("/jizhang")
    else:
        form = ItemForm(request,initial={'pub_date':timezone.now().date()})

    return render(request, template_name,{'form':form})


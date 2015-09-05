#coding=utf-8
from django import forms
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from django.forms import ModelForm
from django.forms.extras.widgets import SelectDateWidget

# Register your models here.
from jizhang.models import Item, Category
from jizhang.data_format_func import sort_category

		
class CategoryForm(ModelForm):

    class Meta:
        model = Category
        fields = ('name', 'p_category', 'isIncome')


    def __init__(self, request, *args, **kwargs):
        super(CategoryForm, self).__init__(*args, **kwargs)
        self.user = request.user
        aa=[]
        for category in Category.objects.filter(user__username=request.user.username):
            if not category.p_category:
                aa.extend([[category.id,  category.name, 0]])
            else:
                aa.extend([[category.id,  category.name, category.p_category.id]])

        category_sort,row_start = sort_category(aa,0,0,0)
        bb=[(cate[0], cate[1])  for cate in category_sort]
        self.fields['p_category'].widget = forms.Select(attrs={'class':"form-control"})
        self.fields['p_category'].choices = [('',u'----------------')] + bb

        self.fields['name'].widget = forms.TextInput(attrs={'class':"form-control"})
        self.fields['isIncome'].widget = forms.CheckboxInput(attrs={'checkbox':True})

    def clean_isIncome(self):
        if self.cleaned_data['p_category']:
            if not self.cleaned_data['p_category'].isIncome==self.cleaned_data['isIncome']:
                raise forms.ValidationError(u"是否收入应和父类别一致.")	
        return self.cleaned_data['isIncome']

    def save(self):
        new_category = Category(name=self.cleaned_data['name'],
        p_category=self.cleaned_data['p_category'],
        user = self.user,
        isIncome=self.cleaned_data['isIncome'])
        return new_category

class NewCategoryForm(CategoryForm):

	# new category name must not repeat
    def clean_name(self):
        try:
            # user = request.user
            repeat_category = Category.objects.get(name=self.cleaned_data['name'])
        except Category.DoesNotExist:
            return self.cleaned_data['name']
        raise forms.ValidationError(u"该名称类别已有，请使用其他的名称.")	


class ItemForm(ModelForm):

    class Meta:
        model = Item
        fields = ('pub_date', 'category', 'price', 'comment')

    def save(self):
        new_item = Item(category=self.cleaned_data['category'],
            price=self.cleaned_data['price'],
            pub_date=self.cleaned_data['pub_date'],
            comment=self.cleaned_data['comment'])
        if not new_item.category.isIncome:
            if new_item.price>0:
                new_item.price = new_item.price*-1
        else:
            if new_item.price<0:
                new_item.price = new_item.price*-1
                
        return new_item

    def __init__(self, request, *args, **kwargs):
        super(ItemForm, self).__init__(*args, **kwargs)
        aa=[]
        for category in Category.objects.filter(user__username=request.user.username):
            if not category.p_category:
                aa.extend([[category.id,  category.name, 0]])
            else:
                aa.extend([[category.id,  category.name, category.p_category.id]])

        category_sort,row_start = sort_category(aa,0,0,0)
        bb=[(cate[0], cate[1]) for cate in category_sort]
        
        self.fields['category'].widget = forms.Select(attrs={'class':"form-control"})
        self.fields['category'].choices = bb
        
        self.fields['pub_date'].widget = forms.DateInput(attrs={'class':"datepicker form-control"})
        self.fields['price'].widget = forms.TextInput(attrs={'class':"form-control"})
        self.fields['comment'].widget = forms.TextInput(attrs={'class':"form-control"})


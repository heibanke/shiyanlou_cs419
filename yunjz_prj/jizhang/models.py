#coding=utf-8
from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

# Create your models here.

class Category(models.Model):
    INCOME_CHOICES = (
        (True, u'收入'),
        (False, u'支出'),
    )
    p_category = models.ForeignKey('self', null = True, blank = True, verbose_name=u"父类名称", related_name='childs')
    name = models.CharField(max_length=20, verbose_name=u"类别名称")
    isIncome = models.BooleanField(choices=INCOME_CHOICES, verbose_name=u'是否收入')
    user = models.ForeignKey(User,verbose_name=u'所属用户')

    def __str__(self):
        return self.level()+self.name

    def get_absolute_url(self):
        return '%s' % (reverse('jizhang:edit_category', args=(self.id,))) 

    def get_items_url(self):
        return '%s' % (reverse('jizhang:show_category', args=(self.id,))) 
    
    #shiyan7
    def level(self):
        if self.p_category:
            return "----"+self.p_category.level()
        else:
            return ""
    
    #shiyan7
    def save(self, *args, **kwargs):
        #form保证了子类不能修改isIncome，只能修改顶级父类的isIncome
        #遍历一遍childs，统一设置isIncome
        for child in self.childs.all():
            if child.isIncome != self.isIncome:
                child.isIncome = self.isIncome
                child.save()
                
        super(self.__class__, self).save(*args, **kwargs)        

class Item(models.Model):
    price = models.DecimalField(max_digits=20, decimal_places=2, verbose_name=u'金额')
    comment = models.CharField(max_length=200, blank = True, verbose_name=u'注释')
    pub_date = models.DateField(verbose_name=u'日期')
    category = models.ForeignKey(Category,verbose_name=u'分类', related_name='items')  

    def __str__(self):
        return str(self.price)

    def get_absolute_url(self):
        return '%s' % (reverse('jizhang:edit_item', args=(self.id,))) 
    
    def get_price(self):
        if self.category.isIncome:
            return self.price
        else:
            return -1*self.price

    def save(self, *args, **kwargs):
        if self.price<0:
            self.price = -1*self.price
        super(self.__class__, self).save(*args, **kwargs)

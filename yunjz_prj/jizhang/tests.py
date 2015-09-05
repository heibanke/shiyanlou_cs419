#coding=utf-8

from django.test import TestCase
from django.test import Client
from django.contrib.auth.models import User  
from django.contrib.auth import authenticate
from django.contrib.auth.models import check_password
from django.core.urlresolvers import reverse

from jizhang.forms import ItemForm, CategoryForm, NewCategoryForm
from jizhang.models import Item, Category


PASSWORD = "test123456"

def init_data():
    category1 = Category.objects.create()
    category1.save()
    item1 = Item.objects.create()
    item1.save()
    return item1,category1

# Create your tests here.
class ItemsPageTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="test", email="test@123.com", password=PASSWORD)
        self.user.save()
        self.item,self.category = init_data()
        self.client = Client(enforce_csrf_checks=True)
        self.client.login(username=self.user.username, password=PASSWORD)
        
    def test_items_get(self):
        # GET request.
        response = self.client.get(reverse('jizhang:items'))
        # Check that the response is 200 OK.
        self.assertEqual(response.status_code, 200)
        
"""
    def test_edit_item(self):
        # POST request
        response = self.client.post(reverse('jizhang:edit_item',self.item.id),
                {'username': self.user.username, 'password': PASSWORD})
        #print response.content
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response,reverse('accounts:index'))
        
    def test_login_post_noactive(self):
        # POST request
        response = self.client.post(reverse('accounts:login'),{'username': self.no_active_user.username, 'password': PASSWORD})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['error'], u'用户'+self.no_active_user.username+u'没有激活')
        
    def test_login_post_wrong(self):
        # POST request
        response = self.client.post(reverse('accounts:login'),{'username': self.fail_username, 'password': PASSWORD})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['error'], u'用户'+self.fail_username+u'不存在')
        
class IndexPageTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testindex", email="test@123.com", password=PASSWORD)
        self.user.save()
        self.client = Client()  
        
    def test_login_success(self):    
        self.assertEqual(True,self.client.login(username= self.user.username, password= PASSWORD))
        response = self.client.get(reverse('accounts:index'))
        self.assertEqual(response.status_code, 200)       

    def test_nologin(self):    
        response = self.client.get(reverse('accounts:index'))
        self.assertEqual(response.status_code, 302)  
        self.assertRedirects(response, '/accounts/login/?next=/accounts/index')
        

class RegisterFormTestCase(TestCase):   
    def setUp(self):
        self.correct_data = {"username":"test","email":"test@123.com",
                "password":PASSWORD,"re_password":PASSWORD}
                
    def test_empty(self):
        form=RegisterForm({})
        self.assertFalse(form.is_valid())
        self.assertTrue(form['username'].errors)
        self.assertTrue(form['email'].errors)
        self.assertTrue(form['password'].errors)
        self.assertTrue(form['re_password'].errors) 
        self.assertTrue(form.non_field_errors)
        
    def test_correct(self):
        form=RegisterForm(self.correct_data)
        self.assertTrue(form.is_valid())

class RegisterPageTestCase(TestCase):   
    def setUp(self):
        self.correct_data = {"username":"test","email":"test@123.com",
                "password":PASSWORD,"re_password":PASSWORD}
        self.client = Client()  
        
    def test_empty(self):
        response = self.client.post(reverse('accounts:register'),{})
        self.assertTrue(response.context['form']['email'])
        self.assertTrue(response.context['form']['username'])
        
    def test_correct(self):
        response = self.client.post(reverse('accounts:register'),self.correct_data)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response,reverse('accounts:index'))    

"""    

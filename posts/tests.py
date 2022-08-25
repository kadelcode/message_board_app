from cgitb import text
from django.test import TestCase
from .models import Post
from django.urls import reverse

# Create your tests here.

#Test for Model
class PostModelTest(TestCase):
    #create a new db with one entry
    def setUp(self) :
        Post.objects.create(text = 'This is a test case')
    
    #check if the db field(text) is actually 'This is a test case'
    def test_text_content(self):
        post = Post.objects.get(id = 1)
        expected_object_name = f'{post.text}'# f strings which allows us to put variables in our strings.
        self.assertEqual(expected_object_name, 'This is a test case')

#Test for Homepage
class HomePageTest(TestCase):
    #creating the post object in db
    def setUp(self):
        Post.objects.create(text = 'The homepage test')

    #test if the view exist at a url('/')
    def test_view_exists_at_url(self):
        resp = self.client.get('/')
        self.assertEqual(resp.status_code, 200)

    #test if the view has the name = 'home'
    def test_view_exists_by_name(self):
        resp = self.client.get(reverse('home'))
        self.assertEqual(resp.status_code, 200)

    #test if the view uses the correct template('index.html')
    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('home'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'index.html')
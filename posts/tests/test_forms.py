from django.test import TestCase
from posts.models import Post
from posts.forms import PostForm
from django.utils import timezone


class PostFormsTestCase(TestCase):
    def test_valid_form(self):
        obj = Post.objects.create(title='New post', body='body_to_TEST_the_title')
        data = {"title": obj.title, 'body': obj.body, 'image': None, 'pub_date': timezone.now()}
        form = PostForm(data=data)
        self.assertFalse(form.is_valid())
        self.assertEqual(form.cleaned_data.get('title'), obj.title)

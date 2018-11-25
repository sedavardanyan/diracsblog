from django.test import TestCase
from posts.models import Post
from django.utils import timezone


class PostModelTestCase(TestCase):
    def setUp(self):
        Post.objects.create(title='New post', body='body_to_TEST_the_title')

    def test_post_title(self):
        obj = Post.objects.get(body='body_to_TEST_the_title')
        self.assertEqual(obj.title, "New post")

    def test_image_name(self):
        obj = Post.objects.get(body='body_to_TEST_the_title')
        self.assertTrue(obj.image.name == "")

    def create_post(self, title="Title1"):
        return Post.objects.create(title=title)

    def test_pot_pub_date(self):
        obj1 = self.create_post(title="Title1")
        obj2 = self.create_post(title="Title1")
        self.assertEqual(obj1.pub_date, obj2.pub_date)
        self.assertIsInstance(obj1.pub_date, timezone.datetime)
        self.assertIsInstance(obj2.pub_date_pretty(), str)

    def test_summary_len(self):
        obj1 = self.create_post(title="Title1")
        obj2 = self.create_post(title="Title1")
        self.assertLess(len(obj1.summary()), 100)
        self.assertEqual(obj1.summary(), obj2.summary())

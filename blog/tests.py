from django.test import TestCase

from django.contrib.auth import get_user_model #import get_user_model to reference our active User
from django.urls import reverse
from . import models
# Create your tests here.

class BlogTests(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username = "testuser",
            email = "test@email.com",
            password = "secret"
        )

        self.post = models.Post.objects.create(
            title = "A good title",
            text = "This is testing the body content",
            author = self.user
        )

    def test_string_representation(self):
        post = models.Post(title = "A sample title")
        self.assertEqual(str(post), post.title)

    def test_post_content(self):
        self.assertEqual(f"{self.post.title}", "A good title")
        self.assertEqual(f"{self.post.author}", "testuser")
        self.assertEqual(f"{self.post.text}", "This is testing the body content")

    def test_post_list_view(self):
        response = self.client.get(reverse("blog:posts"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "A good title")
        self.assertTemplateUsed(response, "blog/blog_list.html")

    def test_post_detail_view(self):
        response = self.client.get("/blog/1/")
        no_response = self.client.get("/blog/10000000/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, 'This is testing the body content')
        self.assertTemplateUsed(response, 'blog/blog_detail.html')

from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from .models import Sweet

# Create your tests here.

class SweetsTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
             username="sara",
             email="sara@email.com", 
             password="test123"
        )

        self.sweet = Sweet.objects.create(
            name="cake", purchaser=self.user, flavor="vanilla" , count = 2
        )
    
    def test_string_representation(self):
        self.assertEqual(str(self.sweet), "cake")

    def test_sweet_content(self):
        self.assertEqual(f"{self.sweet.name}", "cake")
        self.assertEqual(f"{self.sweet.purchaser}", "sara@email.com")
        self.assertEqual(f"{self.sweet.flavor}","vanilla")
        self.assertEqual(self.sweet.count, 2)


    def test_sweet_list_view(self):
        response = self.client.get(reverse("list"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "cake")
        self.assertTemplateUsed(response, "sweets/list.html")

    def test_sweet_detail_view(self):
        response = self.client.get(reverse("detail", args="1"))
        no_response = self.client.get("/100000/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, "Purchaser: sara@email.com")
        self.assertTemplateUsed(response, "sweets/detail.html")

    def test_sweet_create_view(self):
        response = self.client.post(
            reverse("create"),
            {
                "name": "cookies",
                "purchaser": self.user.id,
                "flavor": "chocolate",
                "count": 5
            }, follow=True
        )

        self.assertRedirects(response, reverse("detail", args="2"))
        self.assertContains(response, "cookies")


    def test_sweet_update_view_redirect(self):
        response = self.client.post(
            reverse("update", args="1"),
            {"name": "cupcake","purchaser":self.user.id,"flavor":"chocolate", "count": 5}
        )

        self.assertRedirects(response, reverse("detail", args="1"))

    def test_sweet_delete_view(self):
        response = self.client.get(reverse("delete", args="1"))
        self.assertEqual(response.status_code, 200)
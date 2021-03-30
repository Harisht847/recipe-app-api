from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse


class AdminSiteTests(TestCase):

    def setUp(self):
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(email="admin@gmail.com",password='test123')
        self.client.force_login(self.admin_user)
        self.user = get_user_model().objects.create_user(
            email = "testing@gmail.com",
            password='test123',
            name='test user'
            )

    def test_users_listed(self):
        """Test users listed on user page """
        url = reverse('admin:core_user_changelist')
        res = self.client.get(url)

        self.assertContains(res, self.user.name)
        self.assertContains(res, self.user.email)
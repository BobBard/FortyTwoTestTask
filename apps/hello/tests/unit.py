from django.test import TestCase
from django.test.client import RequestFactory

from apps.hello.views import HomeView
from testing_utils import populate_test_db


class RequestTests(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        # populate_test_db()

    def test_home_view_without_client(self):
        """
        Test for request content and response code
        :return:
        """
        request = self.factory.get('/')
        response = HomeView(request)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "42 Coffee Cups Test Assignment")
        self.assertContains(response, "Borys")
        self.assertContains(response, "Bardysh")
        self.assertContains(response, "Olegovych")
        self.assertContains(response, "11.06.1990")
        self.assertContains(response, "borys.bardysh@synergy-way.com")
        self.assertContains(response, "bobbard@42cc.co")
        self.assertContains(response, "id")

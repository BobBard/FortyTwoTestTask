from django import test
from django.contrib.auth.models import AnonymousUser
from django.test.client import RequestFactory

from apps.hello.models import UserData
from apps.hello.views import HomeView


class RequestTests(test.TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        UserData.objects.create(username='Borys',
                                surname="Bardysh",
                                email='borys.bardysh@synergy-way.com',
                                bio="Developer at synergy-way",
                                birth_date="1990-11-06",
                                jabber="bobbard@42cc.co",
                                skype="id",
                                other_contacts="")

    def test_home_view(self):
        """
        Test for request content and response code
        :return:
        """
        request = self.factory.get('/')
        request.user = AnonymousUser()
        response = HomeView.as_view()(request)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "42 Coffee Cups Test Assignment")
        self.assertContains(response, "Borys")
        self.assertContains(response, "Bardysh")
        self.assertContains(response, "Nov. 6, 1990")
        self.assertContains(response, "borys.bardysh@synergy-way.com")
        self.assertContains(response, "bobbard@42cc.co")
        self.assertContains(response, "id")

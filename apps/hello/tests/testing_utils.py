from apps.hello.models import UserData
from django.contrib.auth.models import User


def populate_test_db():
    user1 = User.objects.create_user(username='Borys',
                                     email='borys.bardysh@synergy-way.com',
                                     password='11061990')

    UserData.objects.create(pk=user1.id,
                            surname="Bardysh",
                            bio="Olegovych",
                            jabber="bobbard@42cc.co",
                            skype="id",
                            other_contacts="")

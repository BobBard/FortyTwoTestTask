from django.contrib.auth.models import User
from django.forms.models import model_to_dict
from django.shortcuts import render
from django.views.generic import View

from apps.hello.models import UserData


class HomeView(View):
    def get_user_data(self):
        user = User.objects.get_or_create(email='borys.bardysh@synergy-way.com',
                                          username='Borys',
                                          password='11061990')[0]
        userdata = UserData.objects.get_or_create(user=user,
                                                  surname="Bardysh",
                                                  bio="Developer at synergy-way",
                                                  birth_date="1990-11-06",
                                                  jabber="bobbard@42cc.co",
                                                  skype="id",
                                                  other_contacts="")[0]
        result = dict(model_to_dict(user), **model_to_dict(userdata))
        return result

    def get(self, request):
        result = self.get_user_data()
        return render(request, 'hello/home.html', result)

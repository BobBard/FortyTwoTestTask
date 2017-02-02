from django.contrib.auth.models import User
from django.forms.models import model_to_dict
from django.shortcuts import render
from django.views.generic import View

from apps.hello.models import UserData


class HomeView(View):
    def _initial_data(self):
        user1 = User.objects.create_user(username='Borys',
                                         email='borys.bardysh@synergy-way.com',
                                         password='11061990')

        UserData.objects.create(user=user1,
                                surname="Bardysh",
                                bio="Developer at synergy-way",
                                birth_date="1990-11-06",
                                jabber="bobbard@42cc.co",
                                skype="id",
                                other_contacts="")
        userdata = UserData.objects.all()[0]
        user = User.objects.get(id=userdata.user_id)
        result = model_to_dict(user)
        result.update(model_to_dict(userdata))
        return result

    def get(self, request):
        userdata = UserData.objects.all()[0]
        user = User.objects.get(id=userdata.user_id)
        result = model_to_dict(user)
        result.update(model_to_dict(userdata))
        if not result.get('surname'):
            result = self._initial_data()
        return render(request, 'hello/home.html', result)

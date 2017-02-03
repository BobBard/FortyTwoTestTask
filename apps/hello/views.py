from django.forms.models import model_to_dict
from django.shortcuts import render
from django.views.generic import View

from apps.hello.models import UserData


class HomeView(View):
    def get_user_data(self):
        userdata = UserData.objects.get_or_create(
            username='Borys',
            surname='Bardysh',
            email='borys.bardysh@synergy-way.com',
            bio='Developer at synergy-way',
            birth_date='1990-11-06',
            jabber='bobbard@42cc.co',
            skype='id',
            other_contacts='')[0]
        return model_to_dict(userdata)

    def get(self, request):
        result = self.get_user_data()
        return render(request, 'hello/home.html', result)

from django.views.generic import TemplateView
from django.core.urlresolvers import reverse_lazy
from users.models import User


class UsersIndex(TemplateView):
    template_name = 'Users/user.html'

    def get_context_data(self, **kwargs):
        context = super(UsersIndex, self).get_context_data(**kwargs)
        context['user'] = User.objects.all()
        return context
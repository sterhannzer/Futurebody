from django.views.generic import TemplateView, FormView
from django.core.urlresolvers import reverse_lazy
from users.forms import UserForm
from users.models import User


class UsersIndex(TemplateView):
    template_name = 'Users/user.html'

    def get_context_data(self, **kwargs):
        context = super(UsersIndex, self).get_context_data(**kwargs)
        context['users'] = User.objects.all()
        return context


class AddUser(FormView):
    template_name = 'Users/add.html'
    form_class = UserForm
    success_url = reverse_lazy('users_app:user')

    def form_valid(self, form):
        form.save()
        return super(AddUser, self).form_invalid(form)


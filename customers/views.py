# -*- coding: utf-8 -*-
from django.views.generic import TemplateView, FormView
from django.views.generic.edit import UpdateView
from django.core.urlresolvers import reverse_lazy
from datetime import datetime, timedelta
from customers.forms import UserForm
from customers.models import Customer


class UsersIndex(TemplateView):
    template_name = 'Users/user.html'

    def get_context_data(self, **kwargs):
        context = super(UsersIndex, self).get_context_data(**kwargs)
        context['users'] = Customer.objects.all()
        return context


class AddUser(FormView):
    template_name = 'Users/add.html'
    form_class = UserForm
    success_url = reverse_lazy('users_app:user')

    def form_valid(self, form):
        form.save()
        return super(AddUser, self).form_invalid(form)


class UsersShow(TemplateView):
    template_name = 'Users/show.html'

    def how_many_days(self, date_finish_card):  # liczba dni nie bedzie ujemna
        if date_finish_card.days == 1:
            return str(1) + " dzień"
        if date_finish_card.days < 0:
            return str(0) + " dni"
        else:
            return str(date_finish_card.days) + " dni"

    def get_context_data(self, **kwargs):
        context = super(UsersShow, self).get_context_data(**kwargs)
        context['users'] = Customer.objects.get(id=kwargs['id'])
        user = context['users']
        date_finish_card = user.card.date_of_finish - datetime.now().date()
        context['card'] = user.card
        context['days'] = self.how_many_days(date_finish_card)
        context['active'] = user.card.date_of_finish > datetime.now().date()
        return context


class UpdateUser(UpdateView):
    model = Customer
    template_name = 'Users/add.html'
    pk_url_kwarg = "id"
    success_url = reverse_lazy('users_app:user')
    fields = [
        'name',
        'surname',
        'barcode',
        'card'
    ]


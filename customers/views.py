# -*- coding: utf-8 -*-
from django.views.generic import TemplateView, FormView
from django.views.generic.edit import UpdateView
from django.core.urlresolvers import reverse_lazy
from datetime import datetime
from card.models import Card
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
    success_url = reverse_lazy('cards_app:add')

    def form_valid(self, form):
        form.save()
        return super(AddUser, self).form_valid(form)


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
        context['cards'] = Card.objects.filter(customer=context['users'])
        cards = context['cards']
        for card in cards:
            date_finish_card = card.date_of_finish - datetime.now().date()
            card.days = self.how_many_days(date_finish_card)
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
    ]


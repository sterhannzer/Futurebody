from django.http import HttpResponseRedirect
from django.views.generic import FormView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy

from datetime import datetime, timedelta

from card.forms import CardForm, CardEntranceForm
from card.models import Card, CardEntrance


class AddCard(FormView):
    template_name = "Cards/add.html"
    form_class = CardForm
    initial = {'date_of_purchase': datetime.now(),
               'date_of_finish': datetime.now() + timedelta(days=30)}

    def form_valid(self, form):
        form.save()
        return HttpResponseRedirect(
            reverse_lazy('users_app:details', kwargs={'id': form.instance.customer.id})
        )


class AddEntranceCard(FormView):
    template_name = "Cards/add_entrance.html"
    form_class = CardEntranceForm
    success_url = reverse_lazy('users_app:user')
    initial = {'date_of_purchase': datetime.now()}

    def form_valid(self, form):
        form.save()
        return HttpResponseRedirect(
            reverse_lazy('users_app:details', kwargs={'id': form.instance.customer.id})
        )


class CardEdit(UpdateView):
    model = Card
    success_url = reverse_lazy('users_app:user')
    template_name = 'Cards/edit.html'
    pk_url_kwarg = 'id'
    fields = [
        'type',
        'price',
        'date_of_purchase',
        'date_of_finish'
    ]

    def get_initial(self):
        return {
            'date_of_purchase': datetime.now(),
            'date_of_finish': datetime.now()+timedelta(days=30)
        }


class EntranceCardEdit(UpdateView):
    model = CardEntrance
    success_url = reverse_lazy('users_app:user')
    template_name = 'Cards/edit_entrance.html'
    pk_url_kwarg = 'id'
    fields = [
        'price',
        'number_entry'
    ]


class CardDelete(DeleteView):
    model = Card
    success_url = reverse_lazy('users_app:user')
    pk_url_kwarg = 'id'
    template_name = 'Cards/delete.html'


class EntranceCardDelete(DeleteView):
    model = CardEntrance
    success_url = reverse_lazy('users_app:user')
    pk_url_kwarg = 'id'
    template_name = 'Cards/delete.html'

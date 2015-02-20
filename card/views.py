from django.views.generic import FormView, UpdateView
from django.core.urlresolvers import reverse_lazy
from datetime import datetime, timedelta

from card.forms import CardForm
from card.models import Card


class AddCard(FormView):
    template_name = "Cards/add.html"
    form_class = CardForm
    success_url = reverse_lazy('users_app:user')
    initial = {'date_of_purchase': datetime.now(), 'date_of_finish': datetime.now()+timedelta(days=30)}

    def form_valid(self, form):
        form.save()
        return super(AddCard, self).form_valid(form)


class CardEdit(UpdateView):
    model = Card
    success_url = reverse_lazy('users_app:user')
    template_name = 'Cards/add.html'
    pk_url_kwarg = 'id'
    fields = [
        'type',
        'price',
        'date_of_purchase',
        'date_of_finish'
    ]

    def get_initial(self):
        return {'date_of_purchase': datetime.now(), 'date_of_finish': datetime.now()+timedelta(days=30)}

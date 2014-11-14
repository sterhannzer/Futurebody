from django.views.generic import FormView, UpdateView
from django.core.urlresolvers import reverse_lazy
from card.forms import CardForm
from card.models import Card
from users.models import User


class AddCard(FormView):
    template_name = "Cards/add.html"
    form_class = CardForm
    success_url = reverse_lazy('users_app:add')

    def form_valid(self, form):
        form.save()
        return super(AddCard, self).form_invalid(form)


class CardEdit(UpdateView):
    model = Card
    success_url = reverse_lazy('users_app:user')
    template_name = 'Cards/add.html'
    pk_url_kwarg = 'id'
    fields = [
        'name',
        'type',
        'price',
        'date_of_purchase',
        'date_of_finish'
    ]



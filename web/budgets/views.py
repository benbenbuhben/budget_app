from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy
from .models import Budget, Transaction
from .forms import BudgetForm, TransactionForm


class BudgetListView(LoginRequiredMixin, ListView):
    template_name = 'board/budget_list.html'
    context_object_name = 'budgets'
    login_url = reverse_lazy('login')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['transactions'] = Transaction.objects.filter(
            budget__user__username=self.request.user.username)
        print('change')
        return context

    def get_queryset(self):
        return Budget.objects.filter(
            user__username=self.request.user.username)


class BudgetCreateView(LoginRequiredMixin, CreateView):
    """."""
    template_name = 'board/budget_create_form.html'
    # model = Budget
    form_class = BudgetForm
    success_url = reverse_lazy('budget_view')
    login_url = reverse_lazy('login')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class TransactionCreateView(LoginRequiredMixin, CreateView):
    """."""
    # We need to figure out how to send context which will be the budget category corresponding to this new transaction. We could possibly handle this by having parameterized endpoints for this view.
    template_name = 'board/transaction_create_form.html'
    # model = Transaction
    context_object_name = 'budgets'

    form_class = TransactionForm
    success_url = reverse_lazy('budget_view')
    login_url = reverse_lazy('login')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class TransactionDetailView(LoginRequiredMixin, DetailView):
    template_name = 'board/transaction_detail.html'
    context_object_name = 'transaction'
    login_url = reverse_lazy('login')
    pk_url_kwarg = 'id'

    def get_queryset(self):
        return Transaction.objects.filter(
            budget__user__username=self.request.user.username)

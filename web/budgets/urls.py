from django.urls import path
from .views import BudgetListView, TransactionDetailView

urlpatterns = [
    path('budget', BudgetListView.as_view(), name='budget_view'),
    path('budget/<int:id>', TransactionDetailView.as_view(), name='transaction_detail'),
]

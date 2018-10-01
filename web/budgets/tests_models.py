from django.test import TestCase
from ..budget_tool.factories import UserFactory, BudgetFactory, TransactionFactory


class TestBudgetModels(TestCase):
    def setUp(self):
        self.budget = BudgetFactory(
            name='test name',
            total_budget=2786
        )

    def test_default_budget_attrs(self):
        self.assertEqual(self.budget.name, 'test name')
        self.assertEqual(self.budget.total_budget, 2786)


class TestTransactionModels(TestCase):
    pass

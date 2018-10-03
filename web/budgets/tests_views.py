from django.test import TestCase, Client
from ..budget_tool.factories import BudgetFactory, TransactionFactory, UserFactory


class TestBudgetViews(TestCase):
    def setUp(self):
        self.user = UserFactory()
        self.user.set_password('secret')
        self.user.save()
        self.c = Client()

    def test_denied_if_no_login(self):
        res = self.c.get('/board/budget', follow=True)
        self.assertEqual(res.status_code, 200)
        self.assertIn(b'class="login-form container"', res.content)

    def test_view_list_when_logged_in(self):
        self.c.login(
            username=self.user.username,
            password='secret'
        )

        budget = BudgetFactory(user=self.user)
        res = self.c.get('/board/budget')

        self.assertIn(budget.name.encode(), res.content)

    def test_lists_only_owned_budgets(self):
        self.c.login(
            username=self.user.username,
            password='secret'
        )

        own_budget = BudgetFactory(user=self.user)
        other_budget = BudgetFactory()

        res = self.c.get('/board/budget')

        self.assertIn(own_budget.name.encode(), res.content)
        self.assertNotIn(other_budget.name.encode(), res.content)

    def test_transactions_listed_in_view(self):
        self.c.login(
            username=self.user.username,
            password='secret'
        )
        budget = BudgetFactory(user=self.user)
        transaction = TransactionFactory(budget=budget)
        res = self.c.get('/board/budget')

        self.assertIn(transaction.description.encode(), res.content)


class TestTransactionViews(TestCase):
    pass


class TestBudgetCreateViews(TestCase):
    """."""

    def setUp(self):
        self.user = UserFactory()
        self.user.set_password('super_secret')
        self.user.save()
        self.c = Client()

    def test_new_budget_view(self):
        self.c.login(
            username=self.user.username,
            password='super_secret'
        )

        res = self.c.get('/board/budget/new')

        self.assertEqual(res.status_code, 200)
        self.assertIn(b'input type="submit"', res.content)
        self.assertIn(b'name="name"', res.content)
        self.assertIn(b'name="description"', res.content)

    def test_create_view_adds_new_budget(self):
        self.c.login(
            username=self.user.username,
            password='super_secret'
        )

        form_data = {
            'name': ' Name thing',
            'total_budget': 1000
        }

        res = self.c.post('/board/budget/add', form_data, follow=True)

        self.assertIn(b'Name thing', res.content)

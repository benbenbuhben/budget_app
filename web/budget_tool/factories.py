import factory
from django.contrib.auth.models import User
from ..budgets.models import Budget, Transaction


class UserFactory(factory.django.DjangoModelFactory):
    """Create a test user for writing tests."""

    class Meta:
        model = User

    username = factory.Faker('user_name')
    email = factory.Faker('email')
    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')


class BudgetFactory(factory.django.DjangoModelFactory):
    """Create a test budget for writing tests."""

    class Meta:
        model = Budget

    user = factory.SubFactory(UserFactory)
    name = factory.Faker('word')
    total_budget = factory.Faker('random_number', digits=4, fix_len=False)


class TransactionFactory(factory.django.DjangoModelFactory):
    """Create a test transaction for writing tests."""

    class Meta:
        model = Transaction

    assigned_to = factory.SubFactory(UserFactory)
    budget = factory.SubFactory(BudgetFactory)
    type = 'Withdrawal'
    amount = factory.Faker('random_number', digits=2, fix_len=False)
    description = factory.Faker('paragraph')

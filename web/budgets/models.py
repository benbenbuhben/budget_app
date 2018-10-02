from django.contrib.auth.models import User
from django.dispatch import receiver
from django.utils import timezone
from django.db import models


class Budget(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='budgets')
    name = models.CharField(max_length=180, default='Untitled')
    total_budget = models.FloatField()

    date_uploaded = models.DateField(auto_now_add=True)
    date_modified = models.DateField(auto_now=True)

    def __repr__(self):
        return '<Budget: {}>'.format(self.name)

    def __str__(self):
        return '{}'.format(self.name)

    @property
    def remaining_budget(self):
        # We need to figure out how to bring in transactions, filter by user, and add up withdrawals.
        return self.total_budget


class Transaction(models.Model):
    budget = models.ForeignKey(Budget, on_delete=models.CASCADE, related_name='transactions')
    description = models.TextField(blank=True, null=True)
    amount = models.FloatField()
    date_uploaded = models.DateField(auto_now_add=True)
    date_modified = models.DateField(auto_now=True)
    date_completed = models.DateField(blank=True, null=True)

    STATES = (
        ('WITHDRAWAL', 'Withdrawal'),
        ('DEPOSIT', 'Deposit'),
    )
    type = models.CharField(
        max_length=16,
        choices=STATES,
        default='Incomplete'
    )

    def __repr__(self):
        return '<Transaction: {} | {}>'.format(self.description, self.type)

    def __str__(self):
        return '{} | {}'.format(self.description, self.type)


# @receiver(models.signals.post_save, sender=Card)
# def set_card_completed_date(sender, instance, **kwargs):
#     """Update the date completed if completed."""
#     if instance.date_completed == 'Complete' and not instance.date_completed:
#         instance.date_completed = timezone.now()
#         instance.save()

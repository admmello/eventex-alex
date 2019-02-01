from datetime import datetime

from django.shortcuts import resolve_url
from django.test import TestCase
from eventex.subscriptions.models import Subscription


class SubscriptionModelTest(TestCase):
    def setUp(self):
        self.obj = Subscription(
            name='Nome Teste',
            cpf='12345678901',
            email='a@a.com',
            phone='1212'
        )
        self.obj.save()

    def test_create(self):
        self.assertTrue(Subscription.objects.exists())

    def test_created_at(self):
        """Subscription must have an auto created_at attr."""
        self.assertIsInstance(self.obj.created_at, datetime)

    def test_str(self):
        self.assertEqual('Nome Teste', str(self.obj))

    def test_oaid_default_to_false(self):
        """By default paid must be False"""
        self.assertEqual(False, self.obj.paid)

    def test_get_absolute_url(self):
        url = resolve_url('subscriptions:detail', self.obj.pk)
        self.assertEqual(url, self.obj.get_absolute_url())

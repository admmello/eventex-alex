from django.core import mail
from django.shortcuts import resolve_url
from django.test import TestCase


class SubscribePostValid(TestCase):
    def setUp(self):
        data = dict(name='nome', cpf='12345678901', email='a@a.com', phone='121212')
        self.client.post(resolve_url('subscriptions:new'), data)
        self.email = mail.outbox[0]

    def test_subscription_email_subject(self):
        email = mail.outbox[0]
        expect = 'Confirmação de  inscrição'

        self.assertEqual(expect, self.email.subject)

    def test_subscription_email_from(self):
        expect = 'contato@eventex.com.br'

        self.assertEqual(expect, self.email.from_email)

    def test_subscription_email_to(self):
        expect = ['contato@eventex.com.br', 'a@a.com']

        self.assertEqual(expect, self.email.to)

    def test_subscription_email_body(self):
        contents = [
            'nome',
            '12345678901',
            'a@a.com',
            '121212',
        ]
        for content in contents:
            with self.subTest():
                self.assertIn(content, self.email.body)

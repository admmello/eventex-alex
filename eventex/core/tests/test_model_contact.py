from django.core.exceptions import ValidationError
from django.test import TestCase
from eventex.core.models import Speaker, Contact


class ContactModelTest(TestCase):
    def setUp(self):
        self.speaker = Speaker.objects.create(
            name='Nome Teste',
            slug='nome-teste',
            photo='http://hbn.link/hopper-pic'
        )

    def test_email(self):
        contact = Contact.objects.create(
            speaker=self.speaker,
            kind=Contact.EMAIL,
            value='a@a.com'
        )

        self.assertTrue(Contact.objects.exists())

    def test_phone(self):
        contact = Contact.objects.create(
            speaker=self.speaker,
            kind=Contact.PHONE,
            value='a@a.com'
        )

        self.assertTrue(Contact.objects.exists())

    def test_choices(self):
        """Contact kind should be limited to E or P"""
        contact = Contact(speaker=self.speaker, kind='A', value='B')
        self.assertRaises(ValidationError, contact.full_clean)

    def test_str(self):
        contact = Contact(
            speaker=self.speaker,
            kind=Contact.EMAIL,
            value='a@a.com'
        )
        self.assertEqual('a@a.com', str(contact))


class ContactManagerTest(TestCase):
    def setUp(self):
        s = Speaker.objects.create(
            name='Nome Palestrante',
            slug='nome-palestrante',
            photo='http://hbn.link/hopper-pic'
        )

        s.contact_set.create(kind=Contact.EMAIL, value='a@a.com')
        s.contact_set.create(kind=Contact.PHONE, value='1212')

    def test_emails(self):
        qs = Contact.objects.emails()
        expected = ['a@a.com']
        self.assertQuerysetEqual(qs, expected, lambda o: o.value)

    def test_phones(self):
        qs = Contact.objects.phones()
        expected = ['1212']
        self.assertQuerysetEqual(qs, expected, lambda o: o.value)

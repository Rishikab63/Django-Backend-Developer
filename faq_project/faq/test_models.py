from django.test import TestCase
from faq.models import FAQ

class FAQModelTest(TestCase):
    def test_faq_creation(self):
        faq = FAQ.objects.create(question="What is Django?", answer="A web framework.")
        self.assertEqual(faq.answer, "A web framework.")

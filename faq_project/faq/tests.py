from django.test import TestCase
from faq.models import FAQ

class FAQModelTest(TestCase):
    def test_create_faq(self):
        faq = FAQ.objects.create(question="What is Django?", answer="A web framework.")
        self.assertEqual(faq.question, "What is Django?")

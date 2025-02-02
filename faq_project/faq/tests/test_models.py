import pytest
from faq.models import FAQ

@pytest.mark.django_db
def test_faq_creation():
    faq = FAQ.objects.create(
        question="What is Django?",
        answer="Django is a web framework."
    )
    assert faq.answer == "Django is a web framework."

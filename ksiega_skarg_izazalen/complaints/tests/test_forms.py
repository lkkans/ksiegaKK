from django.test import TestCase
from complaints.models import Topic, Comment
from complaints.forms import CommentForm

class CommentFormTest(TestCase):
    def setUp(self):
        # Create a Topic instance
        self.topic = Topic.objects.create(title="Test Topic", description="Test description")

    def test_valid_form(self):
        # Test that the form is valid when given valid data
        form_data = {'author': 'Test Author', 'content': 'Test comment content'}
        form = CommentForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        # Test that the form is invalid when given invalid data (missing content)
        form_data = {'author': 'Test Author', 'content': ''}
        form = CommentForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 1)  # Ensure there's one validation error (content is required)



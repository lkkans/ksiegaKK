from django.test import TestCase
from complaints.models import Topic, Comment

class TopicModelTest(TestCase):
    def setUp(self):
        # Create a Topic instance for testing
        self.topic = Topic.objects.create(title="Test Topic", description="Test description")

    def test_topic_creation(self):
        # Test that the topic was created correctly
        topic = self.topic
        self.assertEqual(topic.title, "Test Topic")
        self.assertEqual(topic.description, "Test description")
        self.assertEqual(str(topic), "Test Topic")  # Check string representation of the topic

class CommentModelTest(TestCase):
    def setUp(self):
        # Create a Topic instance
        self.topic = Topic.objects.create(title="Test Topic", description="Test description")
        # Create a Comment instance
        self.comment = Comment.objects.create(topic=self.topic, author="Test Author", content="Test comment content")

    def test_comment_creation(self):
        # Test that the comment was created correctly
        comment = self.comment
        self.assertEqual(comment.author, "Test Author")
        self.assertEqual(comment.content, "Test comment content")
        self.assertEqual(comment.topic, self.topic)  # Check the foreign key relationship
        self.assertEqual(str(comment), "Comment by Test Author on Test Topic")  # Check string representation of the comment

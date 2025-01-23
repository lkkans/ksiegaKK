from django.test import TestCase
from django.urls import reverse
from complaints.models import Topic, Comment

class TopicListViewTest(TestCase):
    def setUp(self):
        # Create a few Topic instances
        self.topic1 = Topic.objects.create(title="Test Topic 1", description="Description 1")
        self.topic2 = Topic.objects.create(title="Test Topic 2", description="Description 2")

    def test_topic_list_view(self):
        # Test that the topic list view renders correctly
        response = self.client.get(reverse('topic_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'complaints/topic_list.html')
        self.assertContains(response, "Test Topic 1")
        self.assertContains(response, "Test Topic 2")

class TopicDetailViewTest(TestCase):
    def setUp(self):
        # Create a Topic instance
        self.topic = Topic.objects.create(title="Test Topic", description="Test description")
        # Create a Comment instance
        self.comment = Comment.objects.create(topic=self.topic, author="Test Author", content="Test comment content")

    def test_topic_detail_view(self):
        # Test that the topic detail view works and displays the topic and comments
        response = self.client.get(reverse('topic_detail', kwargs={'pk': self.topic.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'complaints/topic_detail.html')
        self.assertContains(response, "Test Topic")
        self.assertContains(response, "Test description")
        self.assertContains(response, "Test comment content")

    def test_add_comment(self):
        # Test that a new comment can be added to a topic
        response = self.client.post(reverse('topic_detail', kwargs={'pk': self.topic.pk}), {
            'author': 'Another Author',
            'content': 'New comment content'
        })
        self.assertEqual(response.status_code, 302)  # Check for a redirect after successful form submission
        self.assertRedirects(response, reverse('topic_detail', kwargs={'pk': self.topic.pk}))

        # Check that the comment was added
        new_comment = Comment.objects.get(content="New comment content")
        self.assertEqual(new_comment.author, 'Another Author')
        self.assertEqual(new_comment.content, 'New comment content')

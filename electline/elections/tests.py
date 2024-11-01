from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.utils import timezone

from datetime import timedelta
from .models import Election, Candidate, Vote

User = get_user_model()

class VotingViewsTestCase(TestCase):
    def setUp(self):
        # Initialize the client, create user and election objects
        self.client = Client()
        self.user = User.objects.create_user(matric_no='CSC/23/3986', password='password123')
        self.client.login(matric_no='CSC/23/3986', password='password123')

        # Create elections and candidates
        # Create start and end dates
        start_date = timezone.now() - timedelta(days=1)  # started yesterday
        end_date = timezone.now() + timedelta(days=1)  # ends tomorrow

        # Create elections with start and end dates
        self.election1 = Election.objects.create(
            title="Election 1", slug="election-1", start_date=start_date, end_date=end_date
        )
        self.election2 = Election.objects.create(
            title="Election 2", slug="election-2", start_date=start_date, end_date=end_date, allowed_prefix='MTS, SEN'
        )
        self.candidate1 = Candidate.objects.create(name="Candidate 1", election=self.election1, matric_no='MTS/23/1242')
        self.candidate2 = Candidate.objects.create(name="Candidate 2", election=self.election1, matric_no='MTS/23/1244')

        # Add method to check if the user is allowed to vote
        Election.is_voter_allowed = lambda self, matric_no: matric_no == "CSC/23/3986"

    def test_elections_view(self):
        response = self.client.get(reverse('elections:elections'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(self.election1, response.context['elections'])
        # self.assertNotIn(self.election2, response.context['elections'])  # Only allowed elections should be shown

    def test_vote_view(self):
        response = self.client.get(reverse('elections:vote', args=[self.election1.slug]))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['election'], self.election1)
        self.assertIn(self.candidate1, response.context['candidates'])
        self.assertIn(self.candidate2, response.context['candidates'])

    def test_cast_vote(self):
        # Send POST request to cast a vote
        response = self.client.post(reverse('elections:cast-vote', args=[self.election1.slug, self.candidate1.id]), {'candidate_id': self.candidate1.id})
        
        # Check if the vote was successfully created
        vote_exists = Vote.objects.filter(user=self.user, candidate=self.candidate1, election=self.election1).exists()
        self.assertTrue(vote_exists)

        # Check if the user is redirected to the election page after voting
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, self.election1.get_absolute_url())

from django.test import TestCase
from .models import User, Team, Activity, Workout, Leaderboard

class ModelTests(TestCase):
    def test_create_team(self):
        team = Team.objects.create(name='Marvel', description='Marvel Team')
        self.assertEqual(str(team), 'Marvel')

    def test_create_user(self):
        team = Team.objects.create(name='DC', description='DC Team')
        user = User.objects.create(name='Bruce Wayne', email='bruce@wayne.com', team=team)
        self.assertEqual(str(user), 'Bruce Wayne')

    def test_create_activity(self):
        team = Team.objects.create(name='Marvel', description='Marvel Team')
        user = User.objects.create(name='Peter Parker', email='peter@parker.com', team=team)
        activity = Activity.objects.create(user=user, type='Running', duration=30, date='2023-01-01')
        self.assertEqual(str(activity), 'Peter Parker - Running (2023-01-01)')

    def test_create_workout(self):
        workout = Workout.objects.create(name='Pushups', description='Upper body workout')
        self.assertEqual(str(workout), 'Pushups')

    def test_create_leaderboard(self):
        team = Team.objects.create(name='Marvel', description='Marvel Team')
        leaderboard = Leaderboard.objects.create(team=team, score=100)
        self.assertEqual(str(leaderboard), 'Marvel - 100')

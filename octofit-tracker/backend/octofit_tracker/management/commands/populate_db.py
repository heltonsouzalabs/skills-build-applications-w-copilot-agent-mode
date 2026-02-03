from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Workout, Leaderboard
from django.utils import timezone

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        self.stdout.write('Deleting old data...')
        Leaderboard.objects.all().delete()
        Activity.objects.all().delete()
        Workout.objects.all().delete()
        User.objects.all().delete()
        Team.objects.all().delete()

        self.stdout.write('Creating teams...')
        marvel = Team.objects.create(name='Marvel', description='Marvel Superheroes')
        dc = Team.objects.create(name='DC', description='DC Superheroes')

        self.stdout.write('Creating users...')
        tony = User.objects.create(name='Tony Stark', email='tony@marvel.com', team=marvel)
        steve = User.objects.create(name='Steve Rogers', email='steve@marvel.com', team=marvel)
        bruce = User.objects.create(name='Bruce Wayne', email='bruce@dc.com', team=dc)
        diana = User.objects.create(name='Diana Prince', email='diana@dc.com', team=dc)

        self.stdout.write('Creating activities...')
        Activity.objects.create(user=tony, type='Run', duration=30, date=timezone.now().date())
        Activity.objects.create(user=steve, type='Swim', duration=45, date=timezone.now().date())
        Activity.objects.create(user=bruce, type='Cycle', duration=60, date=timezone.now().date())
        Activity.objects.create(user=diana, type='Yoga', duration=50, date=timezone.now().date())

        self.stdout.write('Creating workouts...')
        w1 = Workout.objects.create(name='Pushups', description='Upper body strength')
        w2 = Workout.objects.create(name='Running', description='Cardio')
        w1.suggested_for.set([tony, bruce])
        w2.suggested_for.set([steve, diana])

        self.stdout.write('Creating leaderboard...')
        Leaderboard.objects.create(user=tony, score=120, rank=1)
        Leaderboard.objects.create(user=steve, score=110, rank=2)
        Leaderboard.objects.create(user=bruce, score=100, rank=3)
        Leaderboard.objects.create(user=diana, score=90, rank=4)

        self.stdout.write(self.style.SUCCESS('Database populated with test data!'))

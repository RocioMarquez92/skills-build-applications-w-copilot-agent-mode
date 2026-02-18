from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Workout, Leaderboard
from django.utils import timezone

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        # Borrar datos existentes
        Leaderboard.objects.all().delete()
        Activity.objects.all().delete()
        Workout.objects.all().delete()
        User.objects.all().delete()
        Team.objects.all().delete()

        # Crear equipos
        marvel = Team.objects.create(name='Marvel', description='Marvel Team')
        dc = Team.objects.create(name='DC', description='DC Team')

        # Crear usuarios
        spiderman = User.objects.create(name='Spider-Man', email='spiderman@marvel.com', team=marvel)
        ironman = User.objects.create(name='Iron Man', email='ironman@marvel.com', team=marvel)
        hulk = User.objects.create(name='Hulk', email='hulk@marvel.com', team=marvel)
        batman = User.objects.create(name='Batman', email='batman@dc.com', team=dc)
        superman = User.objects.create(name='Superman', email='superman@dc.com', team=dc)
        wonderwoman = User.objects.create(name='Wonder Woman', email='wonderwoman@dc.com', team=dc)

        # Crear actividades
        Activity.objects.create(user=spiderman, type='Running', duration=30, date=timezone.now().date())
        Activity.objects.create(user=ironman, type='Cycling', duration=45, date=timezone.now().date())
        Activity.objects.create(user=hulk, type='Swimming', duration=60, date=timezone.now().date())
        Activity.objects.create(user=batman, type='Running', duration=25, date=timezone.now().date())
        Activity.objects.create(user=superman, type='Cycling', duration=50, date=timezone.now().date())
        Activity.objects.create(user=wonderwoman, type='Swimming', duration=55, date=timezone.now().date())

        # Crear workouts
        w1 = Workout.objects.create(name='Push Ups', description='Upper body workout')
        w2 = Workout.objects.create(name='Sit Ups', description='Core workout')
        w3 = Workout.objects.create(name='Squats', description='Leg workout')
        w1.suggested_for.set([spiderman, batman])
        w2.suggested_for.set([ironman, superman])
        w3.suggested_for.set([hulk, wonderwoman])

        # Crear leaderboard
        Leaderboard.objects.create(user=spiderman, score=100)
        Leaderboard.objects.create(user=ironman, score=90)
        Leaderboard.objects.create(user=hulk, score=80)
        Leaderboard.objects.create(user=batman, score=95)
        Leaderboard.objects.create(user=superman, score=85)
        Leaderboard.objects.create(user=wonderwoman, score=88)

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data'))

from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from bson import ObjectId
from datetime import timedelta

class Command(BaseCommand):
    help = 'Populate the database with test data for users, teams, activities, leaderboard, and workouts'

    def handle(self, *args, **kwargs):
        # Clear existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Create users
        users = [
            User(_id=ObjectId(), username='thundergod', email='thundergod@mhigh.edu', password='password123'),
            User(_id=ObjectId(), username='metalgeek', email='metalgeek@mhigh.edu', password='password123'),
            User(_id=ObjectId(), username='zerocool', email='zerocool@mhigh.edu', password='password123'),
            User(_id=ObjectId(), username='crashoverride', email='crashoverride@mhigh.edu', password='password123'),
            User(_id=ObjectId(), username='sleeptoken', email='sleeptoken@mhigh.edu', password='password123'),
        ]
        User.objects.bulk_create(users)

        # Create teams
        team1 = Team(_id=ObjectId(), name='Blue Team')
        team2 = Team(_id=ObjectId(), name='Gold Team')
        team1.save()
        team2.save()
        team1.members.add(users[0], users[1])
        team2.members.add(users[2], users[3], users[4])

        # Create activities
        activities = [
            Activity(_id=ObjectId(), user=users[0], activity_type='Cycling', duration=timedelta(hours=1)),
            Activity(_id=ObjectId(), user=users[1], activity_type='Running', duration=timedelta(hours=2)),
            Activity(_id=ObjectId(), user=users[2], activity_type='Swimming', duration=timedelta(hours=1, minutes=30)),
            Activity(_id=ObjectId(), user=users[3], activity_type='Strength Training', duration=timedelta(minutes=45)),
            Activity(_id=ObjectId(), user=users[4], activity_type='Yoga', duration=timedelta(hours=1)),
        ]
        Activity.objects.bulk_create(activities)

        # Create leaderboard entries
        leaderboard_entries = [
            Leaderboard(_id=ObjectId(), user=users[0], score=100),
            Leaderboard(_id=ObjectId(), user=users[1], score=90),
            Leaderboard(_id=ObjectId(), user=users[2], score=85),
            Leaderboard(_id=ObjectId(), user=users[3], score=80),
            Leaderboard(_id=ObjectId(), user=users[4], score=75),
        ]
        Leaderboard.objects.bulk_create(leaderboard_entries)

        # Create workouts
        workouts = [
            Workout(_id=ObjectId(), name='Cycling Training', description='Endurance cycling workout'),
            Workout(_id=ObjectId(), name='Running Training', description='Marathon preparation workout'),
            Workout(_id=ObjectId(), name='Swimming Training', description='Lap swimming workout'),
            Workout(_id=ObjectId(), name='Strength Training', description='Weightlifting and resistance training'),
            Workout(_id=ObjectId(), name='Yoga Session', description='Relaxation and flexibility workout'),
        ]
        Workout.objects.bulk_create(workouts)

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with test data.'))

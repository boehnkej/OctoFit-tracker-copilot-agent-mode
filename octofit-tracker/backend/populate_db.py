import os
import django
import random
from django.contrib.auth import get_user_model
from octofit_tracker.models import Activity

# Django Setup
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'octofit_tracker.settings')
django.setup()

User = get_user_model()

# Beispiel-Testdaten
USERS = [
    {'username': 'alice', 'email': 'alice@example.com', 'password': 'test1234'},
    {'username': 'bob', 'email': 'bob@example.com', 'password': 'test1234'},
    {'username': 'carol', 'email': 'carol@example.com', 'password': 'test1234'},
]

ACTIVITIES = [
    {'name': 'Laufen', 'duration': 30, 'calories': 250},
    {'name': 'Radfahren', 'duration': 45, 'calories': 400},
    {'name': 'Schwimmen', 'duration': 60, 'calories': 500},
]

def create_users():
    for user_data in USERS:
        user, created = User.objects.get_or_create(username=user_data['username'], defaults={
            'email': user_data['email']
        })
        if created:
            user.set_password(user_data['password'])
            user.save()
        print(f"User {user.username} {'created' if created else 'already exists'}.")

def create_activities():
    users = list(User.objects.all())
    for _ in range(10):
        user = random.choice(users)
        activity_data = random.choice(ACTIVITIES)
        Activity.objects.create(
            user=user,
            name=activity_data['name'],
            duration=activity_data['duration'],
            calories=activity_data['calories']
        )
    print("10 random activities created.")

def main():
    create_users()
    create_activities()

if __name__ == '__main__':
    main()

from typing import Any
from django.core.management.base import BaseCommand, CommandParser
from django.contrib.auth.models import User

import secrets


class Command(BaseCommand):
    help = 'genearte fake users'

    def add_arguments(self, parser: CommandParser) -> None:
        parser.add_argument('users', type=int, help='Users count')

    def handle(self, *args: Any, **options: Any) -> str | None:
        users_count = options.get('users')

        users = []

        for i in range(1, users_count):
            password = secrets.token_urlsafe(10)
            user = User(username=f'FakeUser_{i}', password=password)

            users.append(user)

        User.objects.bulk_create(users)

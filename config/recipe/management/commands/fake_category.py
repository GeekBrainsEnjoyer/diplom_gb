from typing import Any
from django.core.management.base import BaseCommand, CommandParser

from recipe.models import Category


class Command(BaseCommand):
    help = 'genearte fake category'

    def add_arguments(self, parser: CommandParser) -> None:
        parser.add_argument('category', type=str, help='Category name')

    def handle(self, *args: Any, **options: Any) -> str | None:
        category = Category(name=options['category'])
        category.save()

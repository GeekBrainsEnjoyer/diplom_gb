from typing import Any
from django.core.management.base import BaseCommand, CommandParser
from django.utils.crypto import get_random_string
from django.contrib.auth.models import User

from recipe.models import Recipe, Category

from random import randint
import string
from PIL import Image, ImageDraw


class Command(BaseCommand):
    help = 'genearte fake recipes'

    def add_arguments(self, parser: CommandParser) -> None:
        parser.add_argument('recipes', type=int, help='Recipes count')

    def handle(self, *args: Any, **options: Any) -> str | None:
        recipes_count = options.get('recipes')

        recipes = []

        for i in range(1, recipes_count):
            rand_category = Category.objects.get(
                pk=randint(1, int(Category.objects.all().count())))
            rand_name = f'Fake recipe-{i}'
            rand_description = get_random_string(
                255, (string.ascii_letters + ' '))
            rand_steps = get_random_string(255, (string.ascii_letters + ' '))
            rand_cooking_time = f'{randint(1, 180)} min'
            rand_user = User.objects.get(
                pk=randint(1, User.objects.all().count()))

            random_image(f'media/rand_image_{i}.png')

            recipe = Recipe(category=rand_category,
                            name=rand_name,
                            description=rand_description,
                            steps=rand_steps,
                            cooking_time=rand_cooking_time,
                            image=f'rand_image_{i}.png',
                            created_by=rand_user)

            recipes.append(recipe)

        Recipe.objects.bulk_create(recipes)


def random_image(name: str):
    width, height = 50, 50
    image = Image.new("RGB", (width, height), "white")
    draw = ImageDraw.Draw(image)

    for _ in range(10000):
        x = randint(0, width - 1)
        y = randint(0, height - 1)
        color = (randint(0, 255), randint(
            0, 255), randint(0, 255))
        draw.point((x, y), fill=color)

    image.save(name)

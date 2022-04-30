import sys

from django.db import transaction
from django.core.management.base import BaseCommand

from search_app.models import Post
from search_app.factory import PostFactory

class Command(BaseCommand):
    help = "Generates test data"

    def add_arguments(self , parser):
        parser.add_argument('num_posts' , nargs='+' , type=int, help='evid')

    @transaction.atomic
    def handle(self, *args, **kwargs):
        num_posts = kwargs.get('num_posts', 2)
        if isinstance(num_posts, list):
            num_posts = num_posts[0]

        self.stdout.write("Deleting old data...")
        Post.objects.all().delete()

        self.stdout.write(f"Creating {num_posts} new posts...")
        # Create all the posts
        for _ in range(num_posts):
            post = PostFactory()

        self.stdout.write(f"Completed! Created {num_posts} new posts.")
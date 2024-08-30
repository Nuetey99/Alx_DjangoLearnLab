from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from relationship_app.models import Book

class Command(BaseCommand):
    help = 'Set up initial groups and permissions'

    def handle(self, *args, **kwargs):
        # Create groups
        editors_group, created = Group.objects.get_or_create(name='Editors')
        viewers_group, created = Group.objects.get_or_create(name='Viewers')
        admins_group, created = Group.objects.get_or_create(name='Admins')

        # Get permissions
        content_type = ContentType.objects.get_for_model(Book)
        can_view_book = Permission.objects.get(codename='can_view_book', content_type=content_type)
        can_create_book = Permission.objects.get(codename='can_create_book', content_type=content_type)
        can_edit_book = Permission.objects.get(codename='can_edit_book', content_type=content_type)
        can_delete_book = Permission.objects.get(codename='can_delete_book', content_type=content_type)

        # Assign permissions
        editors_group.permissions.add(can_create_book, can_edit_book)
        viewers_group.permissions.add(can_view_book)
        admins_group.permissions.add(can_view_book, can_create_book, can_edit_book, can_delete_book)

        self.stdout.write(self.style.SUCCESS('Groups and permissions have been set up successfully.'))


from django.core.management import BaseCommand

# django-cms-forms-builder Project
from cms_forms_builder_test_project.fixtures import create_test_data


class Command(BaseCommand):
    help = "Create test app data"

    def add_arguments(self, parser):
        super(Command, self).add_arguments(parser)

        parser.add_argument("--fresh", action="store_true", dest="delete_first", default=False,
            help="Delete existing entries.")

    def handle(self, *args, **options):
        create_test_data(delete_first=options.get('delete_first'))

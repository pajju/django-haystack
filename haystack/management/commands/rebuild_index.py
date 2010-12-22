from optparse import make_option
from django.conf import settings
from django.core.management import call_command
from django.core.management.base import BaseCommand, CommandError
from haystack.management.commands.clear_index import Command as ClearCommand
from haystack.management.commands.update_index import Command as UpdateCommand


class Command(BaseCommand):
    help = "Completely rebuilds the search index by removing the old data and then updating."
    option_list = BaseCommand.option_list + ClearCommand.base_options + UpdateCommand.base_options

    option_list += (
        make_option('--backend', action='append', dest='backends', type='string',
            help='The backend to operate on (may be used multiple times; default=all backends)'
        ),
    )

    def handle(self, **options):
        call_command('clear_index', **options)
        call_command('update_index', **options)

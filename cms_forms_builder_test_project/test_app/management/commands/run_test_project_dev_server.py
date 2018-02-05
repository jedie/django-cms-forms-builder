#!/usr/bin/env python3

import os
import sys


print("sys.real_prefix:", getattr(sys, "real_prefix", "-"))
print("sys.prefix:", sys.prefix)


from django.contrib.auth import get_user_model
from django.contrib.staticfiles.management.commands.runserver import Command as RunServerCommand
from django.core.management import call_command

# django-cms-forms-builder Project
from cms_forms_builder_test_project.fixtures import create_test_data


class Command(RunServerCommand):
    """
    Expand django.contrib.staticfiles runserver
    """

    help = "Setup test project and run django developer server"

    def verbose_call(self, command, *args, **kwargs):
        self.stderr.write("_"*79)
        self.stdout.write("Call %r with: %r %r" % (command, args, kwargs))
        call_command(command, *args, **kwargs)

    def handle(self, *args, **options):

        if "RUN_MAIN" not in os.environ:
            # RUN_MAIN added by auto reloader, see: django/utils/autoreload.py
            self.verbose_call("makemigrations") # only for developing ;)
            self.verbose_call("migrate")

            # django.contrib.staticfiles.management.commands.collectstatic.Command
            self.verbose_call("collectstatic", interactive=False, link=True)

            User=get_user_model()
            qs = User.objects.filter(is_active = True, is_superuser=True)
            if qs.count() == 0:
                self.verbose_call("createsuperuser")
                create_test_data()
            else:
                self.stdout.write("Fixtures was created in the past, ok.")

        options["insecure_serving"] = True
        super(Command, self).handle(*args, **options)

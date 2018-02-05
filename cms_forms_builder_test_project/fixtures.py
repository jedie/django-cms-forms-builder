
import logging

from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType

from cms.models import Page

from django_cms_tools.fixtures.pages import CmsPageCreator

log = logging.getLogger(__name__)



def get_permission(model, codename):
    content_type = ContentType.objects.get_for_model(model)
    permission = Permission.objects.get(content_type=content_type, codename=codename)
    return permission


class TestPageCreator(CmsPageCreator):
    placeholder_slots = ("content",)
    # dummy_text_count = 1

    def __init__(self, no, *args, **kwargs):
        self.no = no
        super(TestPageCreator, self).__init__(*args, **kwargs)

    def get_title(self, language_code, lang_name):
        return "Test page %i in %s" % (self.no, lang_name)

    def get_slug(self, language_code, lang_name):
        slug = super(TestPageCreator, self).get_slug(language_code, lang_name)
        log.debug("slug: %r (%r %s)", slug, language_code, lang_name)
        return slug

    def add_plugins(self, page, placeholder):
        return # Don't add any plugins

    # def get_add_plugin_kwargs(self, page, no, placeholder, language_code, lang_name):
    #     """
    #     Return "content" for create the plugin.
    #     Called from self.add_plugins()
    #     """
    #     return {
    #         "plugin_type": "PlainTextPlugin", # publisher_test_app.cms_plugins.PlainTextPlugin
    #         "text": "Dummy plain text plugin no.%i" % self.no
    #     }


def create_test_page(delete_first=False):
    for no in range(1,5):
        page, created = TestPageCreator(no=no, delete_first=delete_first).create()
        if created:
            print("Test page created: '%s'" % page)
        else:
            print("Test page already exists: '%s'" % page)


def create_test_data(delete_first=False):

    if delete_first:
        qs = Page.objects.all()
        log.debug("Delete %i CMS pages...", qs.count())
        qs.delete()

    create_test_page(delete_first=delete_first)

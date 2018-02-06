
"""
    created 2018 by Jens Diemer <django-cms-forms-builder@jensdiemer.de>

"""


import logging

from django.conf import settings
from django.utils.translation import ugettext_lazy as _

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

# django-cms-forms-builder Project
from cms_forms_builder import app_settings, constants
from cms_forms_builder.app_settings import JQUERY_URL
from cms_forms_builder.models import FormsBuilderPluginModel

log = logging.getLogger(__name__)


class FormsBuilderPlugin(CMSPluginBase):
    """
    Plugin to insert one form into a CMS page.
    """
    model = FormsBuilderPluginModel

    name = app_settings.FORMS_PLUGIN_VERBOSE_NAME
    module = app_settings.FORMS_PLUGIN_MODULE_NAME  # For category in "add plugin" list
    require_parent = True if app_settings.FORMS_PLUGIN_PARENT_CLASSES else False
    parent_classes = app_settings.FORMS_PLUGIN_PARENT_CLASSES
    render_template = app_settings.FORMS_PLUGIN_TEMPLATE

    cache = False

    def __repr__(self):
        return str(super(FormsBuilderPlugin, self).__repr__())

    def __str__(self):
        return str(super(FormsBuilderPlugin, self).__str__())

    def render(self, context, instance, placeholder):
        request = context["request"]
        user = request.user
        form_instance = instance.form # # forms_builder.forms.models.Form instance
        if form_instance is None:
            log.info("There is no form for %s (e.g.: form was deleted?)", self)
        else:
            published = form_instance.published(for_user=user)
            if published:
                context["form_instance"] = form_instance
                context["JQUERY_URL"] = JQUERY_URL
            else:
                log.info("Form not published: Hide: %s", form_instance)
        return context

plugin_pool.register_plugin(FormsBuilderPlugin)
assert FormsBuilderPlugin.__name__ == constants.FORM_BUILDER_PLUGIN_NAME

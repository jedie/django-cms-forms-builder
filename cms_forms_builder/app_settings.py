from django.conf import settings
from django.utils.translation import ugettext_lazy as _


# Used for cms_forms_builder.cms_plugins.FormsBuilderPlugin.render_template
FORMS_PLUGIN_TEMPLATE = getattr(settings, "FORMS_PLUGIN_TEMPLATE", "forms/cms_plugin.html")

# For Django CMS category in "add plugin" list
# Used for cms_forms_builder.cms_plugins.FormsBuilderPlugin.module
FORMS_PLUGIN_MODULE_NAME = getattr(settings, "FORMS_PLUGIN_MODULE_NAME", _("Generic"))

# For Django CMS category in "add plugin" list
# Used for cms_forms_builder.cms_plugins.FormsBuilderPlugin.parent_classes
FORMS_PLUGIN_PARENT_CLASSES = getattr(settings, "FORMS_PLUGIN_PARENT_CLASSES", None)

from django.conf import settings
from django.utils.translation import ugettext_lazy as _

# use jQuery from django:
JQUERY_URL = "/static/admin/js/vendor/jquery/jquery.min.js"

#_____________________________________________________________________________
# cms_forms_builder.cms_plugins.FormsBuilderPlugin

# <CMSPlugin>.name
FORMS_PLUGIN_VERBOSE_NAME = getattr(settings, "FORMS_PLUGIN_VERBOSE_NAME", _("Forms Builder"))

# <CMSPlugin>.module
FORMS_PLUGIN_MODULE_NAME = getattr(settings, "FORMS_PLUGIN_MODULE_NAME", _("Generic"))

# <CMSPlugin>.parent_classes
FORMS_PLUGIN_PARENT_CLASSES = getattr(settings, "FORMS_PLUGIN_PARENT_CLASSES", None)

# <CMSPlugin>.render_template
FORMS_PLUGIN_TEMPLATE = getattr(settings, "FORMS_PLUGIN_TEMPLATE", "forms/cms_plugin.html")




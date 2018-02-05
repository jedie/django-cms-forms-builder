

"""
    created 2018 by Jens Diemer <django-cms-forms-builder@jensdiemer.de>
    
"""


import logging

from django.db import models
from django.utils.translation import ugettext_lazy as _

from cms.models.pluginmodel import CMSPlugin

from forms_builder.forms.models import Form

log = logging.getLogger(__name__)



#______________________________________________________________________________
# Form Builder CMS Plugin


class FormsBuilderPluginModel(CMSPlugin):
    form = models.ForeignKey(Form, null=True, on_delete=models.SET_NULL) # forms_builder.forms.models.Form

    def __repr__(self):
        return str(super(CMSPlugin, self).__repr__())

    def __str__(self):
        return "%s" % self.form

    class Meta:
        verbose_name = _("Form")
        verbose_name_plural = _("Forms")

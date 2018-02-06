from django.conf.urls import include, url
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin

import debug_toolbar


urlpatterns = i18n_patterns(
    # https://github.com/stephenmcd/django-forms-builder
    url(r'^forms/', include("forms_builder.forms.urls")),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^__debug__/', include(debug_toolbar.urls)),
    url(r'^', include('cms.urls')),
)

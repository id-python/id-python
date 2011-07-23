
from django.conf.urls.defaults import *
from django.contrib import admin

from mezzanine.core.views import direct_to_template


admin.autodiscover()

# Add the urlpatterns for any custom Django applications here.
# You can also change the ``home`` view to add your own functionality to
# the project's homepage.
urlpatterns = patterns("",
    (r'^grappelli/', include('grappelli_safe.urls')),
    (r'^filebrowser/', include('filebrowser_safe.urls')),
    ("^admin/", include(admin.site.urls)),
    (r'^planet/', include('planet.urls')),
    url("^$", direct_to_template, {"template": "index.html"}, name="home"),
    ("^", include("mezzanine.urls")),
)

# Adds ``MEDIA_URL`` to the context.
handler500 = "mezzanine.core.views.server_error"


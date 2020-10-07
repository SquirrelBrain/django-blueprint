"""
Global URL Configuration
Docs: https://docs.djangoproject.com/en/dev/topics/http/urls/

Function Views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based Views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

urlpatterns = [

    # Django Admin Site
    path('admin/', admin.site.urls),

]

if settings.DEBUG:

    import debug_toolbar

    urlpatterns += [

        # Admin Documentation
        path('admin/doc/', include('django.contrib.admindocs.urls')),

        # Django Debug Toolbar
        path('__debug__/', include(debug_toolbar.urls)),

    ]

    urlpatterns + static(settings.STATIC_URL,
                         document_root=settings.STATIC_ROOT)

    urlpatterns + static(settings.MEDIA_URL,
                         document_root=settings.MEDIA_ROOT)

from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.urls import re_path
from blog import views





urlpatterns = [
    path('admin/', admin.site.urls),
    path('post/<slug:slug>', views.post_detail, name='post_detail'),
    path('contact/', views.contact, name='contact'),
    path('post/<slug:slug>/comment/', views.add_comment, name='add_comment'),
    path('', views.index, name='index'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls)),
    ]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



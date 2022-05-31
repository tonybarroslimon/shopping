import os
#import products.views
import cart.views
import checkout.views
import contact.views
import customers.views
from django.contrib import admin, admindocs
from django.urls import path, re_path
from django.conf.urls import include

admin.autodiscover()

urlpatterns = [
    path('admin/doc/', include('django.contrib.admindocs.urls')),
    path('admin/', admin.site.urls),
    #re_path(r'^accounts/', registration.backends.default.urls),
    #re_path(r'^media(?P<path>, *)$', 'django.views.static.serve', {'document_root':os.path.join(os.path.dirname(__file__), 'static/media/')}),
    #re_path(r'^static(?P<path>, *)$', 'django.views.static.serve', {'document_root':os.path.join(os.path.dirname(__file__), 'static')}),
    re_path(r'^$', products.views.home),
    re_path(r'^pages/', django.contrib.flatpages.urls),
    re_path(r'^products/$', products.views.products),
    re_path(r'^products/(?P<slug>[-\w]+)/$', products.views.product_single),
    #re_path(r'^products/(?P<slug>[-\w]+)/add$', cart.views.add),
    re_path(r'^contact/$', contact.views.contact),
    re_path(r'^cart/$', cart.views.view),
    re_path(r'^cart/add', cart.views.add_to_cart),
    re_path(r'^cart/delete$', cart.views.delete),
    re_path(r'^checkout/', checkout.views.checkout),
]

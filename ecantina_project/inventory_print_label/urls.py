from django.conf.urls import patterns, include, url
from inventory_print_label.views import comic


urlpatterns = patterns('',
    url(r'^inventory/(\d+)/(\d+)/print_labels/comics$', comic.comics_print_labels_page),
)
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^product/$',views.product_list),
    url(r'^product/(?P<pk>\d+)/$',views.product_detail),
]
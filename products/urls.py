from django.conf.urls import url,include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('product',views.productView)

urlpatterns = [
    # url(r'^product/$',views.product_list),
    # url(r'^product/(?P<pk>\d+)/$',views.product_detail),
    url('',include(router.urls))
]